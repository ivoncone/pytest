from lxml import etree

# Your XML data
xml_data = '''
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
    </country>
</data>
'''

ns = {'pago20':'http://www.sat.gob.mx/Pagos20'}

# Parse the XML data
#root = etree.fromstring(xml_data)
file_path = 'output.xml'
tree = etree.parse(file_path)
root = tree.getroot()
# Find the neighbor element
doctoRelacionado = root.find(".//pago20:DoctoRelacionado", namespaces=ns)

# Add a zip code element next to direction
inv = "TIJ45097"
doctoRelacionado.set("folioFactura", inv)


#modified_xml = etree.tostring(root, pretty_print=True).decode()
tree.write(file_path, encoding='utf-8')
#print(modified_xml)
