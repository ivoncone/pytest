import json
from lxml import etree

def json_to_xml(json_data, root_element_name='root'):
    root = etree.Element(root_element_name)
    json_to_xml_recursive(json_data, root)
    return etree.ElementTree(root)

def json_to_xml_recursive(json_data, parent_element):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            element = etree.SubElement(parent_element, str(key))
            json_to_xml_recursive(value, element)
    elif isinstance(json_data, list):
        for item in json_data:
            element = etree.SubElement(parent_element, 'item')
            json_to_xml_recursive(item, element)
    else:
        parent_element.text = str(json_data)

def main():
    # Replace 'input.json' with the path to your JSON file
    with open('data.json', 'r') as json_file:
        json_data = json.load(json_file)

    root_element_name = 'root'  # You can customize the root element name if needed
    xml_tree = json_to_xml(json_data, root_element_name)

    # Replace 'output.xml' with the desired path for the XML file
    xml_tree.write('output.xml', pretty_print=True, encoding='utf-8')

if __name__ == "__main__":
    main()
