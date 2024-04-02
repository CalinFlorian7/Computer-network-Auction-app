import classes
User=classes.User
Product=classes.Product
UserRegistry=classes.UserRegistry
product1=Product("product1",100)
product2=Product("product2",200)
product3=Product("product3",300)
product4=Product("product4",400)
product5=Product("product2",500)
user=User("Vasile")
user1=User("Ion")
user2=User("Maria")
user3=User("Grigore")
user.addProduct(product1)
user.addProduct(product2)
user.addProduct(product3)
user1.addProduct(product1)
user2.addProduct(product5)
user3.addProduct(product1)
userRegistry=UserRegistry()
userRegistry.addUser(user)
userRegistry.addUser(user1)
userRegistry.addUser(user2)
userRegistry.addUser(user3)
userRegistry.addProductForUser("Vasile",product2)
variabila=userRegistry.updateProductFinalPrice("Vasile",productName="product2",updatedPrice=201)
if variabila==None:
    print("s-a facut update la pret")
else:
    print("?????????????????",variabila)

  
variabila=userRegistry.updateProductFinalPrice("Vasile",productName="product2",updatedPrice=20)

print("?????????????????",variabila)
# user.displayUserProducts()
# user1.displayUserProducts()
# user2.displayUserProducts()
# user3.displayUserProducts()


userRegistry.displayUsers()




# product1=Product("Phone", 200, 900)
# product2=Product("Tablet", 300, 900)
# productRegistry =ProductRegistry.getInstance()
# productRegistry.addProduct(product)
# productRegistry.addProduct(product1)
# productRegistry.addProduct(product2)
# print(productRegistry.displayProducts())
# products=productRegistry.getProducts()
# for key in products:
#     print(key)
#     print(products[key])

# registru=ProductRegistry()
# registru.addProduct(product)
# registru.displayProducts()

# productRegistry.displayProducts()

# produs1=Product("Bike", 100, 900)
# dict={}
# dict[produs1.get_name()]=produs1
# for key in dict:
#     print(key)
#     print(dict[key])