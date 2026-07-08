$(document).ready(function() {
    var toc = document.getElementById("local-toc");
    if (!toc) return;
    var data = getTocObject(toc);
    if (!data.ul) return;
    data = data.ul.length > 1 ? data : data.ul[0];

    var template = Handlebars.templates['sidenav'];
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
