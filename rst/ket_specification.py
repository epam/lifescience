"""Build the KET format specification from its own Markdown pages, which stay identical to its source.

Sphinx needs two things the pages do not hold, and they are added while it reads them. The toctree: the nested
list under ``## Contents`` of the start page is the outline (chapters, then their pages) and becomes a hidden
toctree of the start page and of each chapter page; a page missing from it fails the build as "not included in
any toctree". The front matter, which Sphinx does not print: the edition of the start page and the Since and
Query marks of a page become lines under its title, worded as the specification's own editions print them.
Sphinx reports the line numbers of the text it read: on a page that got lines under its title, a warning names a
line two further per inserted line than the file has it, and the toctree lies past the file's last line.
"""
import os
import re

import yaml
from sphinx.errors import ExtensionError

ROOT = 'ketcher/ket-specification'
# The page of a folder in the specification: the start page in ROOT, a chapter's introduction in its folder.
FOLDER_PAGE = 'index'
START = ROOT + '/' + FOLDER_PAGE

_FRONT_MATTER = re.compile(r'\A---\n(.*?)\n---\n', re.DOTALL)
_CONTENTS = re.compile(r'^## Contents[ \t]*\n(.*?)(?=^## |\Z)', re.MULTILINE | re.DOTALL)
# An outline entry links one page of the specification, without an anchor: "  - [Atom](molecules/atom.md)".
_ENTRY = re.compile(r'(?P<indent>[ \t]*)[-*] \[[^\]\n]+\]\((?P<path>[\w./-]+)\.md\)[ \t]*')
_TITLE = re.compile(r'^# .*\n', re.MULTILINE)


def _outline_error(number, line, problem):
    return ValueError('line %d of the Contents %s: %r' % (number, problem, line))


def read_outline(text):
    """Return {parent: [children relative to the parent's folder]} from the start page.

    The start page is the parent of the first-level entries, each first-level entry of the entries nested
    under it; the outline has these two levels and no third. Names are docnames relative to the specification's
    folder.
    """
    contents = _CONTENTS.search(text)
    if contents is None:
        raise ValueError('no "## Contents" section')
    first_line = text.count('\n', 0, contents.start(1)) + 1
    children = {FOLDER_PAGE: []}
    parent = None
    nested_indent = None
    for offset, line in enumerate(contents.group(1).splitlines()):
        number = first_line + offset
        if not line.strip():
            continue
        entry = _ENTRY.fullmatch(line)
        if entry is None:
            raise _outline_error(number, line, 'is not a link to a page')
        path = os.path.normpath(entry.group('path')).replace(os.sep, '/')
        if path.startswith('../') or path.startswith('/'):
            raise _outline_error(number, line, 'leads out of the specification')
        indent = entry.group('indent')
        if not indent:
            parent = path
            children[FOLDER_PAGE].append(path)
            continue
        if parent is None:
            raise _outline_error(number, line, 'is nested under no entry')
        if nested_indent is None:
            nested_indent = indent
        if indent != nested_indent:
            raise _outline_error(number, line, 'is indented unlike the entries nested above it, or a third level '
                                 'deep; the outline has two levels')
        base = os.path.dirname(parent)
        relative = os.path.relpath(path, base).replace(os.sep, '/') if base else path
        if relative.startswith('../'):
            raise _outline_error(number, line, 'is outside the folder of %s.md' % parent)
        children.setdefault(parent, []).append(relative)
    return {parent: entries for parent, entries in children.items() if entries}


def front_matter(text):
    """Return the fields of a page's front matter, {} for a page without one."""
    found = _FRONT_MATTER.match(text)
    fields = yaml.safe_load(found.group(1)) if found else {}
    if not isinstance(fields, dict):
        raise ValueError('the front matter is not a mapping')
    return fields


def edition_line(fields):
    missing = [key for key in ('format-version', 'status', 'date') if not fields.get(key)]
    if missing:
        raise ValueError('the front matter has no %s' % ', '.join(missing))
    return '*Describes KET %s. Status: %s, %s.*' % (fields['format-version'], fields['status'], fields['date'])


def mark_lines(fields):
    lines = []
    if fields.get('since'):
        lines.append('**Since:** KET %s' % fields['since'])
    if fields.get('query') is True:
        lines.append('*(Query)*')
    return lines


def with_lines_under_title(text, lines):
    front = _FRONT_MATTER.match(text)
    title = _TITLE.search(text, front.end() if front else 0)
    if title is None:
        raise ValueError('no "# " title')
    return '%s\n%s\n\n%s' % (text[:title.end()], '\n\n'.join(lines), text[title.end():].lstrip('\n'))


def with_toctree(text, entries):
    return '%s\n\n```{toctree}\n:hidden:\n\n%s\n```\n' % (text.rstrip('\n'), '\n'.join(entries))


class _Specification:
    def __init__(self):
        self.toctrees = {}

    def load(self, app):
        path = os.path.join(app.srcdir, START + '.md')
        try:
            with open(path, encoding='utf-8') as f:
                outline = read_outline(f.read())
        except (OSError, ValueError) as error:
            raise ExtensionError('ket_specification: %s: %s' % (path, error)) from error
        self.toctrees = {ROOT + '/' + parent: entries for parent, entries in outline.items()}

    def outdated(self, app, env, added, changed, removed):
        # A changed outline changes the toctree of pages that did not change themselves.
        if START in added or START in changed:
            return [name for name in env.found_docs if name.startswith(ROOT + '/')]
        return []

    def inject(self, app, docname, source):
        if not docname.startswith(ROOT + '/'):
            return
        text = source[0]
        try:
            fields = front_matter(text)
            lines = ([edition_line(fields)] if docname == START else []) + mark_lines(fields)
            if lines:
                text = with_lines_under_title(text, lines)
            if docname in self.toctrees:
                text = with_toctree(text, self.toctrees[docname])
        except (ValueError, yaml.YAMLError) as error:
            raise ExtensionError('ket_specification: %s.md: %s' % (docname, error)) from error
        source[0] = text


def setup(app):
    specification = _Specification()
    app.connect('builder-inited', specification.load)
    app.connect('env-get-outdated', specification.outdated)
    app.connect('source-read', specification.inject)
    return {'parallel_read_safe': True}
