import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
num_codes = []
char_codes = []
for node in elements:
    charcode = None
    numcode = None
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    charcode = child.firstChild.data.strip()
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    numcode = child.firstChild.data.strip()
    if charcode and numcode:
        char_codes.append(charcode)
        num_codes.append(numcode)

print("CharCode:", char_codes)
print("NumCode:", num_codes)

xml_file.close()
