import classes
Client=classes.Client
Endpoint=classes.Endpoint



client=Client("127.0.0.1",1234)
client.connect()
# client.insertUser(Endpoint.INSERTUSER.value)

while True:
    print("Write am option from below to continue:")
    print("1. Add product")
    print("2. Start auction")
    chosenOption=input("Your choise option: ")


# while True:
#     name=input("Enter name: ")
#     client.insertUser(name,Endpoint.INSERTUSER.value)
#     response=client.receive_data() 
#     if response!=None: 
#         print("Received response: ",response)

client.close()