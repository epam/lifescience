$(document).ready(function() {
    var toc = document.getElementById("local-toc");
    var data = getTocObject(toc);
    data = data.ul.length > 1 ? data : data.ul[0];

    var htmlstring =
        '{{#each ul}}' +
        '<div class="panel accordion-item">' +
        '    {{#if ul}}' +
        '    <div class="accordion-heading">' +
        '        <p class="accordion-title">' +
        '           <a data-toggle="collapse" data-parent="#accordion1"' +
        '               class="accordion-toggle" href="#item{{@index}}">{{text}}</a>' +
        '        </p>' +
        '    </div>' +
        '    <div class="accordion-collapse collapse in" id="item{{@index}}">' +
        '        <div class="accordion-body">' +
        '            <ul>' +
        '                {{#each ul}}' +
        '                <li><a href="{{href}}">{{text}}</a></li>' +
        '                {{/each}}' +
        '            </ul>' +
        '        </div>' +
        '    </div>' +
        '    {{else}}' +
        '    <div class="accordion-heading">' +
        '        <p class="accordion-title">' +
        '            <a data-parent="#accordion1" class="accordion-toggle" href="{{href}}">{{text}}</a>' +
        '        </p>' +
        '    </div>' +
        '    {{/if}}' +
        '</div>' +
        '{{/each}}';

    var template = Handlebars.compile(htmlstring);
    $('#accordion1').append(template(data));

    function getTocObject(current) {
        var newNode = {};
        var child;
        for (var i = 0; i < current.children.length; i++) {
            child = current.children[i];

            if (child.localName == "ul") {
                newNode["ul"] = [];
                for (var j = 0; j < child.children.length; j++)
                    newNode["ul"].push(getTocObject(child.children[j]))
            } else {
                newNode["text"] = child.innerHTML;
                newNode["href"] = child.attributes["href"].nodeValue;
            }
        }
        return newNode;
    }
});
