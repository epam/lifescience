import os

_SIDENAV_JS = """\
(function() {
    window.Handlebars = window.Handlebars || {};
    var templates = Handlebars.templates = Handlebars.templates || {};
    templates['sidenav'] = function(data) {
        var html = '';
        var items = data.ul || [];
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            html += '<div class="panel accordion-item">';
            if (item.ul) {
                html += '<div class="accordion-heading">' +
                    '<p class="accordion-title">' +
                    '<a data-toggle="collapse" data-parent="#accordion1"' +
                    ' class="accordion-toggle collapsed" href="#item' + i + '">' + item.text + '</a>' +
                    '</p></div>' +
                    '<div class="accordion-collapse collapse" id="item' + i + '">' +
                    '<div class="accordion-body"><ul>';
                for (var j = 0; j < item.ul.length; j++) {
                    html += '<li><a href="' + item.ul[j].href + '">' + item.ul[j].text + '</a></li>';
                }
                html += '</ul></div></div>';
            } else {
                html += '<div class="accordion-heading">' +
                    '<p class="accordion-title">' +
                    '<a data-parent="#accordion1" class="accordion-toggle"' +
                    ' href="' + item.href + '">' + item.text + '</a>' +
                    '</p></div>';
            }
            html += '</div>';
        }
        return html;
    };
})();
"""


def _write_sidenav_template(app):
    dest = os.path.join(
        os.path.dirname(__file__),
        'themes', 'lifescience-theme', 'static', 'js', 'sidenav-template.js'
    )
    with open(dest, 'w') as f:
        f.write(_SIDENAV_JS)


def setup(app):
    app.connect('builder-inited', _write_sidenav_template)
