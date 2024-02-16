import openpyxl
import xml.etree.ElementTree as ET 

def to_xml(xlsx_file_path, xml_file_path):
	wb = openpyxl.load_workbook(xlsx_file_path)
	sheet = wb.active 
	root = ET.Element("root")

	for row in sheet.iter_rows(min_row=2, values_only=True):
		item_element = ET.SubElement(root, "item")

		for header, value in zip(sheet[1], row):
			field_element = ET.SubElement(item_element, str(header.value))
			field_element.text = str(value)

	xml_tree = ET.ElementTree(root)

	with open(xml_file_path, "wb") as xml_file:
		xml_tree.write(xml_file, encoding="utf-8", xml_declaration=True)


xlsx_file_path = "compra_2.xlsx"
xml_file_path = "output2.xml"
to_xml(xlsx_file_path, xml_file_path)