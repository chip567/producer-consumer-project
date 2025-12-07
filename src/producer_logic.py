import time
from src.generator import generate_random_student
from src.buffer_system import empty, full, mutex, buffer

def producer():
    counter = 1
    while True:
        empty.acquire()
        mutex.acquire()

        s = generate_random_student()
        filename = f"student_data/student{counter}.xml"
        
        
        s.to_xml_file(filename)
        buffer.put(counter)

        print(f"[Producer] Created {filename}")
        
        mutex.release()
        full.release()

        counter = counter + 1 if counter < 10 else 1
        time.sleep(1)

