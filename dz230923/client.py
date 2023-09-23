import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    t = True
    while t:
        mes = input()
        s.sendall(mes.encode('utf-8'))
        if mes == "goodbye":
            t = False
        else:
            data = s.recv(1024)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == "goodbye":
                t = False
