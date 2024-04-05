import classes
Client=classes.Client


client=Client("127.0.0.1",1234)
client.connect()
client.send_data("hello from client")
response=client.receive_data()  
client.close()