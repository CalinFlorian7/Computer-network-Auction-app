import classes
User=classes.User
UserRegistry=classes.UserRegistry
user=User("Vasile")
user1=User("Ion")
user2=User("Maria")
user3=User("Grigore")
userRegistry=UserRegistry.getInstance()
userRegistry.addUser(user)
userRegistry.addUser(user1)
userRegistry.addUser(user2)
userRegistry.addUser(user3)
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