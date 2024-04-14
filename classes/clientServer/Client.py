
import socket
import asyncio
import threading
from classes.product.Product import Product
from classes.product.ProductRegistry import ProductRegistry
import json
import time
from classes.endpoint.Endpoint import Endpoint
import select
class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.receiveDataThread = threading.Thread(target=self.receive_data)
        self.sendDataThread = threading.Thread(target=self.send_data)
    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            
            print("Welcome to the auction!")
            self.receiveDataThread.start()
            self.sendDataThread.start()
        except ConnectionRefusedError:
            print("Failed to connect to the server.")
            exit(1)
    
    def send_data(self):
        try:
            while True:
                data=input("Your response: ")
                self.client_socket.sendall(data.encode())
                print("Data sent successfully!")
        except socket.error as e:
            print("Failed to send data:", str(e))
    def receive_data(self):
        try:
            while True:
                data = self.client_socket.recv(1024).decode()
                print("Message  from server:")
                print(data)
        except socket.error as e:
            print("Failed to receive data:", str(e))
            
            
    def isNumber(self,value):
        try:
            val=float(value)
            return True
        except ValueError:
            return False
    # def insertUser(self,endpoint):
    #     try:

    #         print("To begin the auction, please enter your name: ")
    #         while True:
    #             userName = input()
    #             if userName=="":
    #                 print("Please enter a valid name!")
    #             else:
    #                 json_data={"endpoint":endpoint,"userName":userName}
    #                 json_data=json.dumps(json_data)
             
                    
    #                 self.send_data(json_data)
                    
    #                 response=self.receive_data()
    #                 if(response=="error"):
    #                     self.displayError("This name is already taken, please enter another name:")
    #                 else:
    #                     print(response)
    #                     self.isUserInserted=True
    #                     # self.enterAuction()
    #                     self.enterAuctionThread.start()
    #                     self.bidThread.start()
    #                     self.bidThread.join()
                     
    #                     break
   
        # except socket.error as e:
        #     print("Failed to send data:", str(e))
    # def insertProduct(self, endpoint):
    #     try:
            
    #         while True:
    #             productName =""
    #             startingPrice=""
    #             while True:
    #                 productName=input("Please enter the name for the product: ")
    #                 if productName=="":
    #                     print("Please enter a valid product name!")
    #                 else:
    #                     break
    #             while True:
    #                 startingPrice=input("Please enter the starting price for the product: ")
    #                 if startingPrice=="" or self.isNumber(startingPrice)==False or float(startingPrice)<=0:
    #                     print("Please enter a valid product price!")
    #                 else:
    #                     break
                
    #             product=Product(productName,startingPrice) 
    #             product=product.serialize()   
    #             jsonData={"endpoint":endpoint, "product":product}
    #             jsonData=json.dumps(jsonData)
    #             self.send_data(jsonData)
    #             # print("Data sent successfully to the server!")
                
    #             response=self.receive_data()
    #             if(response=="error"):
    #                 print("The product already exists, please enter another product name:")
    #             else:
    #                 print("The product was added!")
    #                 break
    #     except socket.error as e:
    #         print("Failed to send data:", str(e))
    
    # def startAuction(self,endpoint):
    #     try:
            
    #         self.displayProducts()
    #         products=self.getProducts()
    #         if products==None:
    #             self.displayError("No products available! Please add a product first!")
    #             return
    #         productName=input("To start an auction, please enter the name of the product: ")
    #         while True:
    #             if productName not in products:
    #                 print("The product does not exist, please enter a valid product name!")
    #                 productName=input("To start an auction, please enter the name of the product: ")
    #             else:
    #                 productForAuction=products[productName]
    #                 productForAuction=productForAuction.serialize()
    #                 jsonData={"endpoint":Endpoint.STARTAUCTION.value,"product":productForAuction}
    #                 jsonData=json.dumps(jsonData)
    #                 self.send_data(jsonData)
                
    #                 response=self.receive_data()
    #                 if(response=="started"):
    #                     print("The auction has started!")
    #                     self.startBidding()
    #                 # else:
    #                 #     if response is not None:
    #                 #         self.displayError("Mesaj de la licitatie"+response)
                        
    #                 break

       
    #     except socket.error as e:
    #         print("Failed to send data:", str(e))

    
        

    # def enterAuction(self):
    #     print("esti in meniu")
        
       
    #     while True:
    #         print("----------------------------------------------------------------------")
    #         print("Write am option from below to continue:")
    #         print("1. Add product")
    #         print("2. Start an auction")
    #         print("3. Get products")
   
    #         chosenOption=input("Your choise option: ")
    #         if(chosenOption=="1"):
    #             self.insertProduct(Endpoint.INSERTPRODUCT.value)
    #         if(chosenOption=="2"):
    #             self.startAuction(Endpoint.STARTAUCTION.value)
    #         if(chosenOption=="3"):
    #             self.displayProducts()
    #             # if products==None:
    #             #     self.displayError("No products available! Please add a product first!")
    #             # else:
    #             #     print("Your products:")
    #             #     for index,product in products.items():
    #             #         print(" Product name: "+product.getName()+" ,Starting price: "+str(product.getStartingPrice()))

        
    # def getProducts(self):
    #     try:
    #         jsonData={"endpoint":Endpoint.GETPRODUCTS.value}
    #         jsonData=json.dumps(jsonData)
    #         self.send_data(jsonData)
    #         print("request to recieve products send!")
    #         response=self.receive_data()
            
          
    #         if(response=="error"):
    #             return None
    #         else:
    #             response=json.loads(response)
    #             products=ProductRegistry.deserialize(response)
    #             return products
               
                    
        
    #     except socket.error as e:
    #         print("Failed to send data:", str(e))
    # def displayProducts(self):
    #     try:
    #         jsonData={"endpoint":Endpoint.GETPRODUCTS.value}
    #         jsonData=json.dumps(jsonData)
    #         self.send_data(jsonData)
    #         print("request to recieve products send!")
    #         response=self.receive_data()
            
          
    #         if(response=="error"):
    #             print("No products available! Please add a product first!")
    #         else:
    #             print(response)
    #             response=json.loads(response)
    #             products=ProductRegistry.deserialize(response)
    #             for key,product in products.items():
    #                 product.displayProductNameAndStartingPrice()
    #     except socket.error as e:
    #         print("Failed to send data:", str(e))

    # def startBidding(self):
    #     self.isUserBidding=True
    #     while True:
    #         response=self.receive_data()
    #         if response is not None and response!="started" :
    #             print("Raspuns incercare licitatie: "+response)
           
    #         while True:
    #             bidPrice=input("Please enter your bid: ")
    #             if bidPrice=="" or self.isNumber(bidPrice)==False or float(bidPrice)<=0:
    #                 print("Please enter a valid bid price!")
    #             else:
    #                 bid_data={"endpoint":Endpoint.BID.value,"bidPrice":bidPrice}
    #                 bid_data=json.dumps(bid_data)
    #                 self.send_data(bid_data)
    #                 break


    
    def close(self):
        self.client_socket.close()
        print("Connection closed.")