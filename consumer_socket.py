import socket
from xml.etree import ElementTree as ET
from src.student import ITstudent
from utils.xml_utils import xml_string_to_student 

def start_consumer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)

    print("[Consumer] Waiting for producer to connect...")
    conn, addr = server.accept()
    print(f"[Consumer] Connected to producer at {addr}")

    buffer = ""

    while True:
        chunk = conn.recv(4096).decode("utf-8")
        if not chunk:
            break

        buffer += chunk
        
        while "\n" in buffer:
             xml_data, buffer = buffer.split("\n", 1)

             if xml_data.strip() == "":
                  continue
        
        
        print("\n[Consumer] Received XML Data:")
        print(xml_data)

        student = xml_string_to_student(xml_data)

        print("\n===== STUDENT DATA RECEIVED OVER NETWORK =====")
        student.display_info()
        print("===============================================\n")

    conn.close()

if __name__ == "__main__":
    start_consumer()


