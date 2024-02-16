import json
import xml.etree.ElementTree as ET

# Load JSON data from file
with open('data.json') as json_file:
    data = json.load(json_file)

root = ET.Element("cfdi:Conceptos")

for entry in data['doctoRelacionados']:
    concepto = ET.SubElement(root, "cfdi:Concepto")
    concepto.set('IdDocumento', entry['IdDocumento'])
    concepto.set('MonedaDR', entry['MonedaDR'])
    concepto.set('folio_facura', entry['folio_facura'])
    concepto.set('NumParcialidad', entry['NumParcialidad'])
    concepto.set('ImpSaldoAnt', entry['ImpSaldoAnt'])
    concepto.set('ImpPagado', entry['ImpPagado'])
    concepto.set('ImpSaldoInsoluto', entry['ImpSaldoInsoluto'])
    concepto.set('ObjetoImpDR', entry['ObjetoImpDR'])
    concepto.set('EquivalenciaDR', entry['EquivalenciaDR'])

tree = ET.ElementTree(root)


tree.write("data.xml", encoding="utf-8", xml_declaration=True)

print("Conversion successful. XML file saved as data.xml")
