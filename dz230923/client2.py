import socket
import threading

# Функция для чтения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'goodbye':
                break
            else:
                print(message)
        
        except ConnectionResetError:
            break

    client_socket.close()

# Функция для отправки сообщений серверу
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.sendall(message.encode())
        if message == 'goodbye':
            break

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    #  поток для чтения сообщений
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    #  поток для отправки сообщений
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    main()
