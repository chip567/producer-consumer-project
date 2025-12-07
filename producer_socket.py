import socket
import time
from src.generator import generate_random_student  

def start_producer():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))
    print("[Producer] Connected to consumer.")

    while True:
        student = generate_random_student()
        xml_data = student.to_xml_string()

        client.send((xml_data + "\n").encode("utf-8"))

        print(f"[Producer] Sent student data:\n{xml_data}\n")

        time.sleep(2)

if __name__ == "__main__":
    start_producer()

