import socket
import threading
from classes.product.Product import Product
from classes.product.ProductRegistry import ProductRegistry
import json
from classes.endpoint.Endpoint import Endpoint
class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
        
        
      

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
           
            print("Welcome to the auction!")
        
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
                    json_data={"endpoint":endpoint,"userName":userName}
             
                    
                    self.client_socket.sendall(json.dumps(json_data).encode())
                    print("Data sent successfully to the server!")
                    response=self.receive_data()
                    if(response=="error"):
                        self.displayError("This name is already taken, please enter another name:")
                    else:
                        print(response)
                        break
    

            
            
           
        except socket.error as e:
            print("Failed to send data:", str(e))
    def insertProduct(self, endpoint):
        try:
            
            while True:
                productName =""
                startingPrice=""
                while True:
                    productName=input("Please enter the name for the product: ")
                    if productName=="":
                        print("Please enter a valid product name!")
                    else:
                        break
                while True:
                    startingPrice=input("Please enter the starting price for the product: ")
                    if startingPrice=="" or self.isNumber(startingPrice)==False:
                        print("Please enter a valid prouct price!")
                    else:
                        break
                
                product=Product(productName,startingPrice) 
                product=product.serialize()   
                jsonData={"endpoint":endpoint, "product":product}
                jsonData=json.dumps(jsonData)
                self.client_socket.sendall(jsonData.encode())
                print("Data sent successfully to the server!")
                response=self.receive_data()
                if(response=="error"):
                    print("The product already exists, please enter another product name:")
                else:
                    print(response)
                    break
        except socket.error as e:
            print("Failed to send data:", str(e))
    def startAuction(self,endpoint):
        try:
            products=self.getProducts()
            print("Your products:")
            for index,product in products.items():
                print(" Product name: "+product.getName()+" ,Starting price: "+str(product.getStartingPrice()))
            productName=input("To start an auction, please enter the name of the product: ")
            while True:
                if productName not in products:
                    print("The product does not exist, please enter a valid product name!")
                    productName=input("To start an auction, please enter the name of the product: ")
                else:
                    break



            
            
        except socket.error as e:
            print("Failed to send data:", str(e))
    def getProducts(self):
        try:
            jsonData={"endpoint":Endpoint.GETPRODUCTS.value}
            jsonData=json.dumps(jsonData)
            self.client_socket.sendall(jsonData.encode())
            print("request to recieve products send!")
            response=self.receive_data()
          
            if(response=="error"):
                self.displayError("No products available! Please add a product first!")
            else:
                response=json.loads(response)
                products=ProductRegistry.deserialize(response)
                
                return products
        
        except socket.error as e:
            print("Failed to send data:", str(e))
    def isNumber(self,value):
        try:
            val=float(value)
            return True
        except ValueError:
            return False
    def receive_data(self):
        try:
            data = self.client_socket.recv(1024).decode()
          
            return data
        except socket.error as e:
            print("Failed to receive data:", str(e))
    def displayError(self,error):
        print("\n--------------------------------------------------------\n")
        print(error)
        print("\n--------------------------------------------------------")
    def close(self):
        self.client_socket.close()
        print("Connection closed.")

