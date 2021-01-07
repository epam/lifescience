import xml.etree.ElementTree as ET

GROUPS = [
    "Cheminformatics",
    "Bioinformatics",
    "Data processing",
    "Software development"
]

GROUP_MAP = {
"Bingo": "Cheminformatics",
"Indigo Toolkit": "Cheminformatics",
"Ketcher": "Cheminformatics",
"Indigo ELN": "Cheminformatics",
"Imago OCR": "Cheminformatics",
"Parso": "Data processing",
"Selenium Framework": "Software development",
"Cloud Pipeline": "Bioinformatics",
"Med3web": "Bioinformatics",
"Miew": "Bioinformatics",
"NGB": "Bioinformatics"
}



def lifesciences_menu(s):
    # print(s)
    # with open ('menu.xml', 'w') as f:
    #     f.write(s)
    ins = s.encode("utf-8")
    root = ET.fromstring(ins)

    group_products = dict()

    for k in GROUPS:
        group_products[k] = []

    for elem in root:
        product_ref = elem.find('a')
        if product_ref.text in GROUP_MAP:
            g = GROUP_MAP[product_ref.text]
        else:
            g = "Software development"
        p = {"name": product_ref.text + " &raquo;", "href": product_ref.attrib["href"]}
        group_products[g].append(p)
        p_refs = elem.find('ul')
        if p_refs is None:
            continue
        p['refs'] = []
        for elem_sub in p_refs:
            elem_sub_ref = elem_sub.find('a')
            p['refs'].append({"name": elem_sub_ref.text, "href": elem_sub_ref.attrib["href"]})
        
    res_items = []

    for group in GROUPS:
        res_items.append({"name": group, "products": group_products[group]})

    return res_items


def add_filters(app):
    app.builder.templates.environment.filters['lifesciences_menu'] = lifesciences_menu

def setup(app):
    app.connect("builder-inited", add_filters)

def local_test():
    with open('menu.xml', 'r') as f:
        s = lifesciences_menu(f.read())
        print(s)


if __name__ == '__main__':
    local_test()


