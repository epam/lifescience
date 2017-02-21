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



def lifesciences_menu(s):
    ins = s.encode("utf-8")
    root = ET.fromstring(ins)

    group_products = dict()

    for k in GROUPS:
        group_products[k] = []

    for elem in root:
        product_ref = elem.find('a')
        g = GROUP_MAP[product_ref.text]
        p = {"name": product_ref.text + " &raquo;", "href": product_ref.attrib["href"]}
        group_products[g].append(p)
        p_refs = elem.find('ul')
        if p_refs is None:
            continue
        p['refs'] = []
        for elem_sub in p_refs:
            elem_sub_ref = elem_sub.find('a')
            p['refs'].append({"name": elem_sub_ref.text, "href": elem_sub_ref.attrib["href"]})

    flat_root = ET.fromstring('<div class="container"></div>')

    for g in GROUPS:
        h = ET.SubElement(flat_root, 'h2')
        h.text = g
        ET.SubElement(flat_root, 'hr')
        div_row = ET.SubElement(flat_root, 'div', attrib={'class':'dropdown-menu-row'} )

        prods = group_products[g]
        for p in prods:
            div = ET.SubElement(div_row, 'div', attrib={'class':'dropdown-menu-column'} )
            span = ET.SubElement(div, 'span', attrib={'class':'nav-subtitle'} )
            a = ET.SubElement(span, 'a', attrib={'class':"reference internal", 'href': p['href']} )
            a.text = p['name']
            if 'refs' in p:
                ul = ET.SubElement(div, 'ul')
                for r in p['refs']:
                    li = ET.SubElement(ul, 'li')
                    a2 = ET.SubElement(li, 'a', attrib={'class':"reference internal",
                                                         'href': r['href']})
                    a2.text = r['name']

    res = ET.tostring(flat_root, encoding="UTF-8", method="html").replace('&amp;', '&')
    return res


def add_filters(app):
    app.builder.templates.environment.filters['lifesciences_menu'] = lifesciences_menu

def setup(app):
    app.connect("builder-inited", add_filters)

def local_test():
    with open('/opt/repo/lifescience/in2.xml', 'r') as f:
        s = lifesciences_menu(f.read())
        print(s)


if __name__ == '__main__':
    local_test()


