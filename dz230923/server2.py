import socket
import threading


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

clients = [] #all clients
    

# Функция для обработки сообщений от клиента
def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            
            if message == 'goodbye':
                client_socket.sendall('goodbye'.encode())
                break
            
            # Отправляем сообщение всем остальным клиентам
            for client in clients:
                if client != client_socket:
                    client.sendall(f'{client_address[1]} send you this message:{message}'.encode())
        
        except ConnectionResetError:
            break
    client_socket.close()
    clients.remove(client_socket)

# Функция для обработки подключения клиентов
def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Новый клиент подключился: {client_address}')
        
        clients.append(client_socket)
        
        # поток для сообщений от клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


def main():
    
    # поток для подключения клиентов
    accept_thread = threading.Thread(target=accept_clients)
    accept_thread.start()
    

if __name__ == "__main__":
    main()
