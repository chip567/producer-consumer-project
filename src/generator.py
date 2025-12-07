import random
from src.student import ITstudent

names = ["Lindiwe", "Sandziswa", "Thabo", "Nhlanhla"]
surnames = ["Maseko", "Nxumalo", "Simelane", "Ngwenya"]
programmes = ["BSc IT", "BSc CS", "BSc IS"]
courses_list = ["CSC411", "CSC312", "CSC222", "CSC111"]

def generate_random_student():
    name = random.choice(names) + " " + random.choice(surnames)
    student_id = str(random.randint(10000000, 99999999))
    programme = random.choice(programmes)

    num_courses = random.randint(1, len(courses_list))
    selected = random.sample(courses_list, num_courses)

    course_marks = {c: random.randint(40, 100) for c in selected}

    return ITstudent(name, student_id, programme, course_marks)

