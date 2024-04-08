import classes
Client=classes.Client
Endpoint=classes.Endpoint


client=Client("127.0.0.1",1234)
client.connect()

while True:
    name=input("Enter name: ")
    client.insertUser(name,Endpoint.INSERTUSER.value)
    response=client.receive_data()  
    print("Received response: ",response)

client.close()