import socket
import threading
from classes import UserRegistry


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
        self.lock = threading.Lock()
        self.users=UserRegistry()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address[0]}:{client_address[1]}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        with self.lock:
            self.connections.append(client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    endpoint,data=message.split("\n")
                    print(f"Recieved endpoint: {endpoint}")
                
                    print(f"Recieved userName: {data}")
                    self.broadcast("salut din partea serverului pt toti", client_socket)
                    
                    # self.sendResponse("salut din partea serverului",client_socket)
                else:
                    with self.lock:
                        self.connections.remove(client_socket)
                    client_socket.close()
                    break
            except ConnectionResetError:
                with self.lock:
                    self.connections.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, sender_socket):
        print("broadcasting message")
        with self.lock:
            for client_socket in self.connections:
                if client_socket != sender_socket:
                    client_socket.send(message.encode())
                    print("broadcasting message to client socket")
    def sendResponse(self, message, sender_socket):
        with self.lock:
            if sender_socket in self.connections:
                    sender_socket.send(message.encode())
             
    def stop(self):
        with self.lock:
            for client_socket in self.connections:
                client_socket.close()
            self.connections.clear()
        self.server_socket.close()
        print("Server stopped")

# Usage example
# server = Server('localhost', 1234)
# server.start()