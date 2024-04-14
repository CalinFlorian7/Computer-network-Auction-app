import socket
import json
import threading
from classes import UserRegistry
from classes.product.ProductRegistry import ProductRegistry
from classes.endpoint.Endpoint import Endpoint
from classes.user.User import User
from classes.product.Product import Product
from classes.auction.Auction import Auction
import time


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
        self.lock = threading.Lock()
        self.users=UserRegistry()
        self.connectedUsers={}
        self.isAuctionStarted = False



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
        self.insertUser(client_socket)
        try:
            while True:
                self.sendResponse("Please select an option:\n1. Add a product\n2. Start an auction\n3.Get my products",client_socket)
                option = self.getResponse(client_socket)
                if option == "1":
                    self.insertProduct(client_socket)
                elif option == "2":
                    self.startAuction(client_socket)
                elif option == "3":
                    self.getProducts(client_socket)
                else:
                    self.sendResponse("Please select an option that you have :)) :",client_socket)


        except ConnectionResetError:
                with self.lock:
                    self.connections.remove(client_socket)
                client_socket.close()
    def startAuction(self,client_socket):
        try:
            if self.isAuctionStarted==True:
                self.sendResponse("You cannot start an auction because an auction is in progress right now",client_socket)
                print("You cannot start an auction because an auction is in progress right now")
                return
            products=self.users.getProductsForUser(self.connectedUsers[client_socket.getpeername()[1]])
            if(products.__len__()==0 or products is None):
                self.sendResponse("No products available for auction! Please add a product first!",client_socket)
                print("No products available for auction!")
            else:
                self.getProducts(client_socket)
                while True:
                    self.sendResponse("Please write a product name to start the auction: ",client_socket)
                    productName = self.getResponse(client_socket)
                    while True:
                        if productName not in products:
                            self.sendResponse("The product does not exist, please enter a valid product name!",client_socket)
                            productName = self.getResponse(client_socket)
                        else:
                            product=products[productName]
                            print("Produs ales pentru licitatie:",product)
                            productForAuction = Product(product['name'], product['startingPrice'])


                            auction=Auction(self.connectedUsers[client_socket.getpeername()[1]],productForAuction)
                            if self.isAuctionStarted==False:
                                self.start_bidding_session(client_socket,auction)
                                break
                            else:
                                self.sendResponse("You cannot start an auction because an auction is in progress right now",client_socket)
                    break

        except ConnectionResetError as e:
            print(str(e))
           
    def start_bidding_session(self,client_socket,auction):
        try:
            print("session started")
            print("Auction started by: ",auction.getOwner())
            self.isAuctionStarted=True
            self.sendResponse("Your auction has started!",client_socket)
            self.broadcast("An auction has started!\nOwner: "+auction.getOwner()+auction.getProduct(),client_socket)
            sessionTime=time.time()+60
            print("The auction will last for 60 seconds")
            while time.time()<sessionTime:
                currentAuctionTime=sessionTime-time.time()
                self.sendResponse("The auction will end in "+str(int(currentAuctionTime))+" seconds",client_socket)
                self.broadcast("The auction will end in "+str(int(currentAuctionTime))+" seconds",client_socket)
                print("The auction will end in "+str(int(currentAuctionTime))+" seconds")

                
                self.sendResponse("Please enter your bid: ",client_socket)
                
                bid = self.getResponse(client_socket)


                if bid=="" or not self.isNumber(bid):
                    self.sendResponse("Please enter a valid bid!",client_socket)
                else:
                    if auction.bid(float(bid),self.connectedUsers[client_socket.getpeername()[1]]) is None:
                        self.broadcast("New bid: "+self.connectedUsers[client_socket.getpeername()[1]]+" "+bid,client_socket)
                        self.sendResponse("You have successfully bid with the price of "+bid+" !",client_socket)
                        print("New bid: "+self.connectedUsers[client_socket.getpeername()[1]]+" "+bid)
                    else:
                        self.sendResponse("Your bid is lower than the current bid, please enter a higher bid!",client_socket)
                        print("Your bid is lower than the current bid, please enter a higher bid!")

            self.isAuctionStarted = False
            self.broadcast("The auction has ended!",client_socket)
            self.sendResponse("Your auction has ended!",client_socket)
            



        except ConnectionResetError as e:
            print(str(e))    


    def getProducts(self,client_socket):
        try:
            products=self.users.getProductsForUser(self.connectedUsers[client_socket.getpeername()[1]])
            if(products.__len__()==0 or products is None):
                self.sendResponse("No products available!",client_socket)
                print("No products available!")
            else:
                products=json.dumps(products)
                print(products.__str__())
                self.sendResponse(products,client_socket)
        except ConnectionResetError as e:
            print(str(e))
    def insertProduct(self,client_socket):
        try:
            while True:
                self.sendResponse("Please enter the product name: ",client_socket)
                productName = self.getResponse(client_socket)
                self.sendResponse("Please enter the starting price: ",client_socket)
                startingPrice = self.getResponse(client_socket)
                if productName == "":
                    self.sendResponse("Please enter a valid product name!",client_socket)
                elif startingPrice == "" or not self.isNumber(startingPrice):
                    self.sendResponse("Please enter a valid starting price!",client_socket)
                else :
                    product=Product(productName,float(startingPrice))
                    response= self.users.addProductForUser(self.connectedUsers[client_socket.getpeername()[1]],product)
                    if response==None:
                        self.sendResponse("The product was added",client_socket)
                        print("The product was added")
                        break
                        # self.users.displayUsers()
                    elif response=="error":
                            self.sendResponse("This product already exist, please choose another name!",client_socket) 
            

        except ConnectionResetError as e:
            print(str(e))

    
    def insertUser(self,client_socket):

        try:
            self.sendResponse("To enter the auction, please enter your username: ",client_socket)
            while True:
                userName = self.getResponse(client_socket)
                if userName == "":
                    self.sendResponse("Please enter a valid username!",client_socket)
                elif self.users.userNameExists(userName):
                    self.sendResponse("The username already exists, please enter another username: ",client_socket)
                else:
                    user=User(userName)
                    self.users.addUser(user)
                    # self.sendResponse("The registration was succesful",client_socket)
                    self.connectedUsers[client_socket.getpeername()[1]]=user.getName()
                    print("The registration was succesful")
                    break
        except ConnectionResetError as e:
            print(str(e))

                  
    def isNumber(self,value):
        try:
            val=float(value)
            return True
        except ValueError:
            return False  
            

        # while True:
        #     try:
               
        #         message = client_socket.recv(1024).decode()
        #         message=json.loads(message)
        #         # print("Received message: ",message)
        #         if message!=None:
                   
                    
        #             endpoint=message["endpoint"]
                   
                   
        #             if endpoint==Endpoint.INSERTUSER.value:
                        
        #                 data=message["userName"]
        #                 if self.users.userNameExists(data):
        #                     self.sendResponse("error",client_socket)
        #                     # print("the user already exists")
        #                 else:
        #                     user=User(data)
        #                     self.users.addUser(user)
        #                     self.sendResponse("The registration was succesful",client_socket)
        #                     self.connectedUsers[client_socket.getpeername()[1]]=user.getName()
        #                     print("The registration was succesful")
        #             elif endpoint==Endpoint.INSERTPRODUCT.value:
        #                product=message["product"]
        #                product=Product.deserialize(product)
        #                response= self.users.addProductForUser(self.connectedUsers[client_socket.getpeername()[1]],product)
        #                if response==None:
        #                     self.sendResponse("The product was added",client_socket)
        #                     # print("The product was added")
        #                     # self.users.displayUsers()
        #                elif response=="error":
        #                        self.sendResponse("error",client_socket) 
        #             elif endpoint==Endpoint.GETPRODUCTS.value:
        #                 products=self.users.getProductsForUser(self.connectedUsers[client_socket.getpeername()[1]])
        #                 if(products.__len__()==0 or products is None):
        #                     self.sendResponse("error",client_socket)
        #                     print("No products available!")
        #                 else:
                            
        #                     products=json.dumps(products)
        #                     print(products.__str__())
        #                     self.sendResponse(products,client_socket)
        #             elif endpoint==Endpoint.STARTAUCTION.value:
        #                 product=message["product"]
        #                 product=Product.deserialize(product)
        #                 product.displayProductNameAndStartingPrice()
        #                 if self.isAuctionStarted == False:
        #                     self.isAuctionStarted=True
        #                     self.broadcast("started",client_socket)
        #                     self.sendResponse("started",client_socket)
        #                     self.start_bidding_session(client_socket,self.connectedUsers[client_socket.getpeername()[1]],product)
        #                 else:
        #                     self.sendResponse("You cannot start an auction because an auction is in progress right now",client_socket)
                        

                        
                        




        #         else:
        #             with self.lock:
        #                 self.connections.remove(client_socket)
        #             client_socket.close()
        #             break
        #     except ConnectionResetError:
        #         with self.lock:
        #             self.connections.remove(client_socket)
        #         client_socket.close()
        #         break
            

        
       
       
    def getResponse(self,client_socket):
        response = client_socket.recv(1024).decode()
        return response                
    def broadcast(self, message, sender_socket):
        
        with self.lock:
            for client_socket in self.connections:
                if client_socket != sender_socket:
                    client_socket.send(message.encode())
                # else:
                #     client_socket.send(("To yourself").encode())
                

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

