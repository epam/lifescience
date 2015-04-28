from collections import defaultdict
import hashlib
import os
import traceback

import re
import sys
from docutils import nodes
from docutils.parsers.rst.directives import images,flag
from sphinx.errors import SphinxError
from sphinx.util import relative_uri
from sphinx import addnodes

global _no_indigo
_no_indigo = False

try:
    from indigo import Indigo, IndigoException
    from indigo_renderer import IndigoRenderer
    from indigo_inchi import IndigoInchi
except Exception as e:
    _no_indigo = True
    print("WARNING: could not load indigo: some images will not be renderred")



from codeblockimport import registerCodeDict

DEFAULT_FORMATS = dict(html='svg', latex='pdf', text=None, xml=None)

indigo = None
indigoRenderer = None
indigoInchi = None

absolutePaths = {}
outputData = defaultdict(str)

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.data = ''

    def write(self, message):
        #self.terminal.write(message)
        global outputData
        outputData[self] += message

    def flush(self):
        self.terminal.flush()

    def read(self):
        return self.data

def resetIndigo():
    global indigo, indigoRenderer, indigoInchi

    indigo = Indigo()
    indigoRenderer = IndigoRenderer(indigo)
    indigoInchi = IndigoInchi(indigo)

    # Set default options
    indigo.setOption('render-bond-length', '30')
    indigo.setOption('render-relative-thickness', '1.3')
    indigo.setOption('render-coloring', False)
    indigo.setOption('render-comment-font-size', 14.0)
    indigo.setOption('render-comment-offset', '10')

def get_hashid(text, options):
    hashkey = text.encode('utf-8') + str(options)
    hashid = hashlib.sha1(hashkey).hexdigest()
    return hashid

class IndigoRendererError(SphinxError):
    category = 'IndigoRenderer error'

class IndigoRendererDirective(images.Figure):
    has_content = True
    required_arguments = 0

    own_option_spec = dict(
        indigooptions = str,
        indigoobjecttype = str,
        indigoloadertype = str,
        includecode = str,
        imagename = str,
        codename = str,
        downloads = str,
        noimage = flag,
        nocode = flag,
        includecodefile = str,
        format = str,
        nooutputtitle = flag,
    )

    option_spec = images.Image.option_spec.copy()
    option_spec.update(own_option_spec)

    def run(self):
        self.arguments = ['']
        indigorenderer_options = dict([(k,v) for k,v in self.options.items()
                                      if k in self.own_option_spec])

        text = '\n'.join(self.content)

        if 'codename' in indigorenderer_options:
            registerCodeDict(indigorenderer_options['codename'], text)

        (image_node,) = images.Image.run(self)
        if isinstance(image_node, nodes.system_message):
            return [image_node, ]

        image_node.indigorenderer = dict(text=text, options=indigorenderer_options)

        blocks = []

        def addImagesNodes ():
            blocks.append(image_node)

        need_code = 'nocode' not in self.options and len(text.strip()) > 0 and indigorenderer_options['indigoobjecttype'] == 'code'

        def addCodeNodes ():
            if need_code:
                literal = nodes.literal_block(text, text, line=self.lineno)
                #literal['linenos'] = True
                literal['language'] = 'python'
                blocks.append(literal)


        def addDownloadsNodes ():
            if 'downloads' in self.options:
                blocks.append(nodes.Text('Input:     '))
                for file in self.options['downloads'].split(','):
                    download = addnodes.download_reference("", "")
                    download += nodes.literal(file, file)
                    download['reftarget'] = file
                    blocks.append(download)
                    blocks.append(nodes.Text('     '))
                blocks.append(nodes.line())

        if need_code:
            addCodeNodes()
            addDownloadsNodes()
            addImagesNodes()
        else:
            addImagesNodes()
            blocks.append(nodes.line())
            addDownloadsNodes()

        return blocks

def render_indigorenderer_images(app, doctree):
    for img in doctree.traverse(nodes.image):
        if not hasattr(img, 'indigorenderer'):
            continue

        text = img.indigorenderer['text']
        options = img.indigorenderer['options']
        try:
            res = render_indigorenderer(app, text, options, os.path.dirname(doctree.attributes['source']), os.path.abspath(os.curdir))
            if res is None:
                continue

            relative_paths, output = res
            imgnodes = []
            if 'noimage' not in options:
                for relative_path in relative_paths:
                    newimg = img.copy()
                    newimg['uri'] = relative_path.replace('\\', '/')
                    newimg['scale'] = 1.0 / float(len(relative_paths))
                    imgnodes.append(newimg)
                    #span = img.copy()
                    #span['uri'] = relative_uri(app.builder.env.docname, '_static') + '/span.png'
                    #imgnodes.append(span)
            if output:
                if 'noimage' not in options:
                    newline = nodes.line()
                    imgnodes.append(newline)
                if 'nooutputtitle' not in options:
                    title = nodes.Text('Output:')
                    imgnodes.append(title)
                literal = nodes.literal_block(output, output)
                literal['classes'] += ['output']
                imgnodes.append(literal)
            img.replace_self(imgnodes)
        except IndigoRendererError, exc:
            app.builder.warn('indigorenderer error: ' + str(exc))
            img.replace_self(nodes.literal_block(text, text))
            continue

def expandRelativePaths (relPath):
    print(os.getcwd())
    if relPath.find("%d") == -1:
        return [relPath]
    paths = []
    for i in range(10):
        path = relPath % (i)
        if os.path.exists(path):
            paths.append(path)
    return paths

def replaceRenderedImages (code, absolute_path, relativePath):
    found = (code.find('result.png') != -1)
    paths = []
    if found:
        code = code.replace('result.png', absolute_path)
        paths.append((absolute_path, relativePath))

    result = re.search('result_(.*)\.png', code, re.MULTILINE)
    while result:
        new_absolute_path = absolute_path.replace('.png', result.group(1) + '.png').replace('.svg', result.group(1) + '.svg').replace('.pdf', result.group(1) + '.pdf')
        new_relative_path = relativePath.replace('.png', result.group(1) + '.png').replace('.svg', result.group(1) + '.svg').replace('.pdf', result.group(1) + '.pdf')
        code = code.replace(result.group(0), new_absolute_path)
        result = re.search('result_(.*)\.png', code, re.MULTILINE)
        found = True
        paths.append((new_absolute_path, new_relative_path))

    return code, paths

def appendRelativePaths (paths, relativePaths):
    for abs_path, rel_path in paths:
        if os.path.exists(abs_path):
            if rel_path not in relativePaths:
                relativePaths.append(rel_path)
        if abs_path.find("%d") != -1:
            for i in range(10):
                if os.path.exists(abs_path % i):
                    if rel_path % i not in relativePaths:
                        relativePaths.append(rel_path % i)


def executeIndigoCode(text, absolute_path, relativePath, rstdir, curdir, options):
    try:
        relativePaths = []

        os.chdir(rstdir)
        logger = Logger()
        sys.stdout = logger

        all_paths = []

        if 'includecode' in options:
            import codeblockimport
            for name in options['includecode'].split(','):
                code = codeblockimport.codeDict[name]
                code, paths = replaceRenderedImages(code, absolute_path, relativePath)
                exec(code, globals())
                all_paths += paths
                appendRelativePaths(all_paths, relativePaths)

        if 'includecodefile' in options:
            codefile = options['includecodefile']
            f = open(codefile)
            code = f.read()
            f.close()
            codedir = os.path.dirname(codefile)
            paths = []
            code, paths = replaceRenderedImages(code, absolute_path, relativePath)
            os.chdir(os.path.join(rstdir, codedir))
            exec(code, globals())
            appendRelativePaths(paths, relativePaths)
            os.chdir(rstdir)

        text, paths = replaceRenderedImages(text, absolute_path, relativePath)
        all_paths += paths
        exec(text, globals())
        appendRelativePaths(all_paths, relativePaths)
        os.chdir(curdir)
        global outputData
        sys.stdout = sys.__stdout__
        return outputData[logger], relativePaths
    except Exception as e:
        traceback.print_exc()

def render(indigo, options, text, absolute_path, relativePath, rstdir, curdir):
    indigo_object_type = options['indigoobjecttype']
    indigo_loader_type = options['indigoloadertype']
    loader = None
    if indigo_object_type == 'molecule':
        if indigo_loader_type == 'text':
            loader = indigo.loadMolecule
        elif indigo_loader_type == 'file':
            loader = indigo.loadMoleculeFromFile
    elif indigo_object_type == 'queryMolecule':
        if indigo_loader_type == 'text':
            loader = indigo.loadQueryMolecule
        elif indigo_loader_type == 'file':
            loader = indigo.loadQueryMoleculeFromFile
    elif indigo_object_type == 'reaction':
        if indigo_loader_type == 'text':
            loader = indigo.loadReaction
        elif indigo_loader_type == 'file':
            loader = indigo.loadReactionFromFile
    elif indigo_object_type == 'queryReaction':
        if indigo_loader_type == 'text':
            loader = indigo.loadQueryReaction
        elif indigo_loader_type == 'file':
            loader = indigo.loadQueryReactionFromFile
    elif indigo_object_type == 'smarts':
        if indigo_loader_type == 'text':
            loader = indigo.loadSmarts
        elif indigo_loader_type == 'file':
            loader = indigo.loadSmartsFromFile
    elif indigo_object_type == 'reactionSmarts':
        if indigo_loader_type == 'text':
            loader = indigo.loadReactionSmarts
        elif indigo_loader_type == 'file':
            loader = indigo.loadReactonSmartsFromFile
    elif indigo_object_type == 'code':
        loader = executeIndigoCode
    if not loader:
        raise IndigoRendererError('Cannot find indigo loader for object type: %s, %s' % (indigo_object_type, indigo_loader_type))
    if loader != executeIndigoCode:
        indigoRenderer.renderToFile(loader(text), absolute_path)
    else:
        return executeIndigoCode(text, absolute_path, relativePath, rstdir, curdir, options)

def render_indigorenderer(app, text, options, rstdir, curdir):
    format_map = DEFAULT_FORMATS.copy()
    format_map.update(app.builder.config.indigorenderer_format)
    output_format = None
    
    if len(app.builder.format) > 0:
        output_format = format_map[app.builder.format]
        
    if 'format' in options:
        output_format = options['format']

    if output_format  is None:
        return

    hashid = get_hashid(text, options)
    output_filename = 'indigorenderer_%s.%s' % (hashid, output_format) if not 'imagename' in options else options['imagename'] + '.' + output_format
    relative_path = ''



    if app.builder.format == 'html':
        output_folder = relative_uri(app.builder.env.docname,'_images')
        relative_path = os.path.join(output_folder, output_filename)
        absolute_path = os.path.join(app.builder.outdir, '_images', output_filename)
    else:
        relative_path = output_filename
        absolute_path = os.path.join(app.builder.outdir, output_filename)
    absolute_path = absolute_path.replace('\\', '\\\\')
    relative_paths = [relative_path, ]
    output = None

    if _no_indigo:
        return relative_paths, output

    # Reset Indigo to use new fresh options
    resetIndigo()

    try:
        if 'indigooptions' in options:
            strings = options['indigooptions'][1:-1].split(';')
            for string in strings:
                key, value = string.split('=')
                indigo.setOption(key, value.replace('"', ''))
        indigo.setOption('render-output-format', output_format)
        result = render(indigo, options, text, absolute_path, relative_path, rstdir, curdir)
        if result:
            output, relative_paths = result
    except IndigoException, exc:
        raise IndigoRendererError(exc)


    return relative_paths, output

def setup(app):
    app.add_directive('indigorenderer', IndigoRendererDirective)
    app.connect('doctree-read', render_indigorenderer_images)
    app.add_config_value('indigorenderer_format', DEFAULT_FORMATS, 'html')
