import classes
User=classes.User
Product = classes.Product
ProductRegistry=classes.ProductRegistry
product=Product("Laptop", 100, 900)
product1=Product("Phone", 200, 900)
product2=Product("Tablet", 300, 900)
productRegistry =ProductRegistry.getInstance()
productRegistry.addProduct(product)
productRegistry.addProduct(product1)
productRegistry.addProduct(product2)
print(productRegistry.displayProducts())
products=productRegistry.getProducts()
for key in products:
    print(key)
    print(products[key])
# productRegistry.displayProducts()

# produs1=Product("Bike", 100, 900)
# dict={}
# dict[produs1.get_name()]=produs1
# for key in dict:
#     print(key)
#     print(dict[key])