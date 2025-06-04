#!/usr/bin/env python3
"""
Module task_03_xml

Provides functions to serialize a Python dictionary to XML format
and to deserialize XML data back into a Python dictionary.

The XML format is simple:
<data>
    <key1>value1</key1>
    <key2>value2</key2>
</data>
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to write the XML data to.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = value
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: A dictionary reconstructed from the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dict = {}
    for child in root:
        dict[child.tag] = child.text
    return dict
