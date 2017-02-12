import os
import xml.etree.ElementTree as ET
import xml.sax.saxutils as saxutils

GROUPS = [
    "Cheminformatics",
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
"Selenium Framework": "Software development"
}

group_cache = dict()

def convert_to_flat(s):
    print("********** start")
    if s in group_cache:
        return group_cache[s]

    print("********** parse")
    
    ins = s.encode("utf-8")
    # print(ins)
    root = ET.fromstring(ins)
    # print("********** parsed")

    group_products = dict()

    for k in GROUPS:
        group_products[k] = []

    for elem in root:
        product_ref = elem.find('a')
        g = GROUP_MAP[product_ref.text]
        p = {"name": product_ref.text, "href": product_ref.attrib["href"]}
        group_products[g].append(p)
        p_refs = elem.find('ul')
        if p_refs is None:
            continue
        p['refs'] = []
        for elem_sub in p_refs:
            elem_sub_ref = elem_sub.find('a')
            p['refs'].append({"name": elem_sub_ref.text, "href": elem_sub_ref.attrib["href"]})
        # print (product_ref.text)
        # print(elem.tag)
    # print(group_products)

    flat_root = ET.fromstring('<div class="row"></div>')


    for g in GROUPS:
        h = ET.SubElement(flat_root, 'h2')
        h.text = g
        ET.SubElement(flat_root, 'hr')
        prods = group_products[g]
        for p in prods:
            divr = ET.SubElement(flat_root, 'div', attrib={'class':'row'} )
            div = ET.SubElement(divr, 'div', attrib={'class':'col-md-2 col-sm-6'} )
            span = ET.SubElement(divr, 'span', attrib={'class':'nav-subtitle'} )
            a = ET.SubElement(span, 'a', attrib={'class':"reference internal", 'href': p['href']} )
            a.text = p['name']

    # res = '\n<div class="col-md-2 col-sm-6"><span class="nav-subtitle"><a class="reference internal" href="selenium.html">Selenium Framework &raquo;</a></span></div>'
    res = ET.tostring(flat_root, encoding="UTF-8", method="html")
    group_cache[s] = res

    # return ET.tostring(flat_root, encoding="UTF-8", method="html")
    return res 
def add_jinja_filters(app):
    app.builder.templates.environment.filters['convert_to_flat'] = convert_to_flat

def setup(app):
    app.connect("builder-inited", add_jinja_filters)

def local_test():
    with open('/opt/repo/lifescience/in2.xml', 'r') as f:
        s = convert_to_flat(f.read())
        print(s)


if __name__ == '__main__':
    local_test()


