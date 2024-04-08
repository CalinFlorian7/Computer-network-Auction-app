import socket
import threading
class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.receive_thread = threading.Thread(target=self.receive_data)
        
        
      

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            # print("Connected to the server!")
            print("Welcome to the auction!")
            # self.receive_thread.start()
        except ConnectionRefusedError:
            print("Failed to connect to the server.")

    def send_data(self, data):
        try:
            self.client_socket.sendall(data.encode())
            print("Data sent successfully!")
        except socket.error as e:
            print("Failed to send data:", str(e))
            
    def insertUser(self,endpoint):
        try:

            print("To begin the auction, please enter your name: ")
            while True:
                userName = input()
                if userName=="":
                    print("Please enter a valid name!")
                else:
                    
                    self.client_socket.sendall((endpoint+"\n"+userName).encode())
                    print("Data sent successfully to the server!")
                    response=self.receive_data()
                    if(response=="error"):
                        print("The user already exists, please enter another name:")
                    else:
                        print(response)
                        break

            
            
           
        except socket.error as e:
            print("Failed to send data:", str(e))

    def receive_data(self):
        try:
            data = self.client_socket.recv(1024).decode()
            # print("Received data:", data)
            return data
        except socket.error as e:
            print("Failed to receive data:", str(e))

    def close(self):
        self.client_socket.close()
        print("Connection closed.")

# Usage example:

# client.close()