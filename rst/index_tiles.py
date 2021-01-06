def index_tiles(s):
    # print(s)

    res_items = []

    res_items.append({
        'path': '1',
        'image': '_images/Bingo.jpg',
        'label': 'Label',
        'title': 'Title',
        'text': 'Text',
        'description': '<li>Description</li>'
    })

    return res_items

def add_filters(app):
    app.builder.templates.environment.filters['index_tiles'] = index_tiles

def setup(app):
    app.connect("builder-inited", add_filters)
