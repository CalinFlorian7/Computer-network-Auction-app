import classes
Client=classes.Client
Endpoint=classes.Endpoint



client=Client("127.0.0.1",1234)
client.connect()
userName=""
client.insertUser(Endpoint.INSERTUSER.value)

while True:
    print("----------------------------------------------------------------------")
    print("Write am option from below to continue:")
    print("1. Add product")
    print("2. Start an auction")
    print("3. Get products")
    chosenOption=input("Your choise option: ")
    if(chosenOption=="1"):
        client.insertProduct(Endpoint.INSERTPRODUCT.value)
    if(chosenOption=="2"):
        client.startAuction(Endpoint.STARTAUCTION.value)
   
    

client.close()