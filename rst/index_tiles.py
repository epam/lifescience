import xml.etree.ElementTree as ET

def index_tiles(data: str):
    # print(s)
    # with open ('tiles.xml', 'w') as f:
    #     f.write(s)

    data_root = ET.fromstring(data.encode('utf-8'))
    res_items = []

    for elem in data_root:
        if 'class' in elem.attrib and elem.attrib['class'] == 'section':
            label_name = ''
            
            for section in elem:
                if section.tag == 'h2':
                    label_name = section.text
                    
                if section.tag == 'ul':
                    for product in section:
                        title = ''
                        path = ''
                        descr = ''
                        image = ''
                        text = ''

                        product_p = product.find('p')
                        if product_p is not None:
                            for p in product_p:
                                if p.tail is not None:
                                    text = p.tail
                            product_a = product_p.find('a')
                            if product_a is not None:
                                path = product_a.attrib['href']
                                title = product_a.text
                            product_img = product_p.find('img')
                            if product_img is not None:
                                image = product_img.attrib['src']
                        

                        product_ul = product.find('ul')
                        if product_ul is not None:
                            descr = ET.tostring(product_ul, encoding="UTF-8", method="html").decode('utf-8')


                        res_items.append({
                            'path': path,
                            'image': image,
                            'label': label_name,
                            'title': title,
                            'text': text,
                            'description': descr
                        })
    return res_items

def add_filters(app):
    app.builder.templates.environment.filters['index_tiles'] = index_tiles

def setup(app):
    app.connect("builder-inited", add_filters)

def local_test():
    with open('tiles.xml', 'r') as f:
        s = index_tiles(f.read())
        print(s)


if __name__ == '__main__':
    local_test()
