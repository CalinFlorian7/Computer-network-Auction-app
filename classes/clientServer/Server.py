import socket
import json
import threading
from classes import UserRegistry
from classes.product.ProductRegistry import ProductRegistry
from classes.endpoint.Endpoint import Endpoint
from classes.user.User import User
from classes.product.Product import Product
# from classes.endpoint import Endpoint


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
        self.lock = threading.Lock()
        self.users=UserRegistry()
        self.connectedUsers={}

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
                # print("client socket: " + client_socket.__str__())
                # print("client remote adress",client_socket.getpeername()[1])
                message = client_socket.recv(1024).decode()
                message=json.loads(message)
                print("Received message: ",message)
                if message!=None:
                    # endpoint,data=message.split("\n")
                    
                    endpoint=message["endpoint"]
                   
                    # print(f"Recieved endpoint: {endpoint}")
                
                    # print(f"Recieved userName: {data}")
                    # self.broadcast("salut din partea serverului pt toti", client_socket)
                    
                    # self.sendResponse("salut din partea serverului",client_socket)
                    if endpoint==Endpoint.INSERTUSER.value:
                        data=message["userName"]
                        if self.users.userNameExists(data):
                            self.sendResponse("error",client_socket)
                            print("the user already exists")
                        else:
                            user=User(data)
                            self.users.addUser(user)
                            self.sendResponse("The registration was succesful",client_socket)
                            self.connectedUsers[client_socket.getpeername()[1]]=user.getName()
                            # for user in self.connectedUsers:
                            #     print("Connected users: "+self.connectedUsers[user])
                            print("The registration  succesful")
                    elif endpoint==Endpoint.INSERTPRODUCT.value:
                       product=message["product"]
                       product=Product.deserialize(product)
                       response= self.users.addProductForUser(self.connectedUsers[client_socket.getpeername()[1]],product)
                       if response==None:
                            self.sendResponse("The product was added",client_socket)
                            print("The product was added")
                            self.users.displayUsers()
                       else:
                               self.sendResponse("error",client_socket) 
                    elif endpoint==Endpoint.GETPRODUCTS.value:
                        products=self.users.getProductsForUser(self.connectedUsers[client_socket.getpeername()[1]])
                        if(products.__len__()==0):
                            self.sendResponse("error",client_socket)
                            print("No products available!")
                        else:
                            # products=products.serialize()
                            products=json.dumps(products)
                            print(products.__str__())
                            self.sendResponse(products,client_socket)




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
        
        with self.lock:
            for client_socket in self.connections:
                if client_socket != sender_socket:
                    client_socket.send(message.encode())
                else:
                    client_socket.send("You".encode())
                
                
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