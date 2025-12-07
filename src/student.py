import xml.etree.ElementTree as ET

class ITstudent:
    def __init__(self, name, student_id, programme, courses):
        self.name = name
        self.student_id = student_id
        self.programme = programme
        self.courses = courses

    def calculate_average(self):
        return sum(self.courses.values()) / len(self.courses)

    def get_result(self):
        return "PASS" if self.calculate_average() >= 50 else "FAIL"

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Programme:", self.programme)
        print("Courses:")
        for c, m in self.courses.items():
            print(f"  {c}: {m}")
        print("Average:", round(self.calculate_average(), 2))
        print("Result:", self.get_result())

    # --- XML FILE for threaded version ---
    def to_xml_file(self, filename):
        from utils.xml_utils import student_to_xml_file
        student_to_xml_file(self, filename)

    # --- XML STRING for socket version ---
    def to_xml_string(self):
        from utils.xml_utils import student_to_xml_string
        return student_to_xml_string(self)

