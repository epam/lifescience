import os

def convert_to_flat(s):
    print("**********", s)
    # re.sub(find, replace, s)
    # return s
    # return u'<ul>
    return '\n<div class="col-md-2 col-sm-6"><span class="nav-subtitle"><a class="reference internal" href="selenium.html">Selenium Framework &raquo;</a></span></div>'

def add_jinja_filters(app):
    app.builder.templates.environment.filters['convert_to_flat'] = convert_to_flat


def setup(app):
    app.connect("builder-inited", add_jinja_filters)
