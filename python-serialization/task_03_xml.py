#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)  # Convert all values to strings for XML

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error writing XML to file: {e}")

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            value = child.text

            # Attempt to convert value to int or float if applicable
            if value is None:
                result[child.tag] = None
            elif value.isdigit():
                result[child.tag] = int(value)
            else:
                try:
                    result[child.tag] = float(value)
                except ValueError:
                    result[child.tag] = value  # Keep as string

        return result

    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error reading XML file: {e}")
        return None
