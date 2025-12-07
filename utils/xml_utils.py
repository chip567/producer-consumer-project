import xml.etree.ElementTree as ET
from src.student import ITstudent
import time
import os

def student_to_xml_file(student, filename):
    root = ET.Element("student")
    
   
    ET.SubElement(root, "name").text = student.name
    ET.SubElement(root, "student_id").text = student.student_id
    ET.SubElement(root, "programme").text = student.programme

    courses_elem = ET.SubElement(root, "courses")
    for course, mark in student.courses.items():
        ET.SubElement(courses_elem, "course", code=course, mark=str(mark))
    
   # xml_string = student.to_xml_string()
    #with open(filename, "W", encoding="ütf-8") as f:
     #   f.write(xml_string)
      #  f.flush()
       # os.fsync(f.fileno())
        #return filename
    
    tree = ET.ElementTree(root)
    time.sleep(0.02)
    tree.write(filename)

def xml_file_to_student(filename):
    from src.student import ITstudent
    while os.path.getsize(filename) == 0:
        time.sleep(0.01)
    tree = ET.parse(filename)
    root = tree.getroot()

    name = root.find("name").text
    student_id = root.find("student_id").text
    programme = root.find("programme").text

    courses = {}
    for c in root.find("courses").findall("course"):
        courses[c.get("code")] = int(c.get("mark"))

    return ITstudent(name, student_id, programme, courses)




def student_to_xml_string(student):
    root = ET.Element("student")

    ET.SubElement(root, "name").text = student.name
    ET.SubElement(root, "student_id").text = student.student_id
    ET.SubElement(root, "programme").text = student.programme

    courses_elem = ET.SubElement(root, "courses")
    for course, mark in student.courses.items():
        ET.SubElement(courses_elem, "course", code=course, mark=str(mark))

    return ET.tostring(root, encoding="unicode")


def xml_string_to_student(xml_str):
    from src.student import ITstudent
    
    root = ET.fromstring(xml_str)

    name = root.find("name").text
    student_id = root.find("student_id").text
    programme = root.find("programme").text

    courses = {}
    for c in root.find("courses").findall("course"):
        courses[c.get("code")] = int(c.get("mark"))

    return ITstudent(name, student_id, programme, courses)

