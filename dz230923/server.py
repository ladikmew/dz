# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        t = True
        while t:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == "goodbye":
                t = False
            else:
                mes = input()
                conn.sendall(mes.encode('utf-8'))
                if mes == "goodbye":
                    t = False
