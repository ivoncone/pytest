from lxml import etree

# Your XML data
file_path = 'output.xml'
# Parse the XML data
tree = etree.parse(file_path)
root = tree.getroot()
ns = {'pago': 'http://www.sat.gob.mx/Pagos20'}
# Find the neighbor element
neighbor_element = root.find(".//DoctoRelacionado[@MonedaDR]", namespaces=ns)

# Set the zip code in the neighbor element
neighbor_element.set("folioFactura", "MXL454878")

# Convert the modified XML back to a string
tree.write(file_path, pretty_print=True, encoding='utf-8')

# Print the modified XML
print('file has been modified')
