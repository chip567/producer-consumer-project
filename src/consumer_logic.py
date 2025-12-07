import time, os
from src.buffer_system import empty, full, mutex, buffer
from utils.xml_utils import xml_file_to_student

def consumer():
    while True:
        full.acquire()
        mutex.acquire()

        file_id = buffer.get()
        filename = f"student_data/student{file_id}.xml"

        mutex.release()
        empty.release()

        student = xml_file_to_student(filename)
        print("\n===== STUDENT DATA =====")
        student.display_info()
        print("========================\n")
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"[Consumer] Deleted {filename}")
            except PermissionError:
                print(f"[Consumer] Warning: File still in use cannot delete {filename}")

        time.sleep(2)

