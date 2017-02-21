$(document).ready(function() {
    var indexBody = document.getElementById("life-sciences-open-source");
    if (!indexBody) return;
    var data = getTiles(indexBody);

    console.log(data);

    var htmlstring =
        '{{#each items}}' +
        '   <div class="col-xs-12 col-sm-6">' +
        '       <div class="tile" onclick="location.href=\'{{href}}\'">' +
        '           <div class="tile-image">' +
        '           <img src="{{image}}" alt="">' +
        '           </div>' +
        '           <div class="tile-content">' +
        '               <div class="tile-text">' +
        '                   <div class="tile-label">{{label}}</div>' +
        '                   <h3>{{title}}</h3>' +
        '                   <p>{{{text}}}</p>' +
        '                   <ul class="tile-description">' +
        '                       {{{description}}}' +
        '                   </ul>' +
        '               </div>' +
        '           </div>' +
        '       </div>' +
        '   </div>' +
        '{{/each}}';

    var template = Handlebars.compile(htmlstring);
    $('#index-tiles').append(template({items: data}));

    function getTiles(current) {
        var tiles = [];
        var child;
        for (var i = 0; i < current.children.length; i++) {
            child = current.children[i];
            if (child.localName != 'div' && !child.classList.contains('section'))
                continue;

            var label, labelName;

            for (var j = 0; j < child.children.length; j++) {
                label = child.children[j];

                if (label.localName == 'h2') labelName = label.innerText.replace('¶', '');
                if (label.localName == 'ul') {

                    for (var k = 0; k < label.children.length; k++) {
                        tiles.push(createTile(label.children[k], labelName));
                    }
                }
            }
        }
        return tiles;
    }

    function createTile(tmp, labelName) {
        var tile = {};
        tile['label'] = labelName;
        tile['href'] = tmp.childNodes[0].href;
        tile['title'] = tmp.childNodes[0].innerText;
        tile['text'] = '';
        for (var index = 1; index < tmp.childNodes.length; index++) {
            var elem = tmp.childNodes[index];
            if (elem.localName == 'ul') {
                tile['description'] = elem.innerHTML;
                continue;
            }
            if (elem.localName == 'img') {
                tile['image'] = elem.src;
                continue;
            }
            if (elem.outerHTML) tile['text'] += elem.outerHTML;
            else tile['text'] += elem.data;
        }
        return tile;
    }
});
