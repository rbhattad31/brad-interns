"""
import json as JS
import xml.etree.ElementTree as ET
with open("example_3", "r") as json_file:
    data = JS.load(json_file);
    root = ET.Element("maths")
    Maths = ET.SubElement(root, "q1")
    Q1 = ET.SubElement(Maths, "q2")
    ET.SubElement(Q1, "question")
    text = data["maths"]["q1"]["question"]
    ET.SubElement(Q1, "options").text = str(data["maths"]["q1"]
                                            ["options"][0])

    ET.SubElement(Q1, "options").text = str(data["maths"]["q1"]
                                            ["options"][1])

    ET.SubElement(Q1, "options").text = str(data["maths"]["q1"]
                                            ["options"][2])

    ET.SubElement(Q1, "options").text = str(data["maths"]["q1"]
                                            ["options"][3])

    ET.SubElement(Q1, "answer").text = str(data["maths"]["q1"]
                                           ["answer"])
    Q2 = ET.SubElement(Maths, "q2")
    ET.SubElement(Q2, "question").text = data["maths"]["q2"]["question"]
    ET.SubElement(Q2, "options").text = str(data["maths"]
                                            ["q2"]
                                            ["options"][0])

    ET.SubElement(Q2, "options").text = str(data["maths"]
                                            ["q2"]
                                            ["options"][1])

    ET.SubElement(Q2, "options").text = str(data["maths"]["q2"]
                                            ["options"][2])

    ET.SubElement(Q2, "options").text = str(data["maths"]["q2"]
                                            ["options"][3])

    ET.SubElement(Q2, "answer").text = str(data["maths"]["q2"]
                                           ["answer"])
    tree = ET.ElementTree(root)
    tree.write("quiz.xml")
"""
import json
import xmltodict
with open("quiz.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
