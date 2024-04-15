
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
                # print(data)
                self.printMessage(data)
        except socket.error as e:
            print("Failed to receive data:", str(e))
            
    def isNumber(self,value):
        try:
            val=float(value)
            return True
        except ValueError:
            return False
    
    def printMessage(self,message):
        print("-----------------------------------------------------------------------------------------------------")
        print(message)
        print("-------------")
    def close(self):
        self.client_socket.close()
        print("Connection closed.")