def send_xml(socket, xml_string):
    socket.send(xml_string.encode())

def receive_xml(socket):
    return socket.recv(4096).decode()

