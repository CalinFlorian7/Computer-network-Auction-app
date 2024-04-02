import socket


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            print("Connected to the server!")
        except ConnectionRefusedError:
            print("Failed to connect to the server.")

    def send_data(self, data):
        try:
            self.client_socket.sendall(data.encode())
            print("Data sent successfully!")
        except socket.error as e:
            print("Failed to send data:", str(e))

    def receive_data(self):
        try:
            data = self.client_socket.recv(1024).decode()
            print("Received data:", data)
            return data
        except socket.error as e:
            print("Failed to receive data:", str(e))

    def close(self):
        self.client_socket.close()
        print("Connection closed.")

# Usage example:
client = Client("127.0.0.1", 1234)  # Replace with your server IP and port
client.connect()
client.send_data("Hello, server!")
response = client.receive_data()
# client.close()