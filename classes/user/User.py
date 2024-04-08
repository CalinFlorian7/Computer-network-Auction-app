
from classes.product.ProductRegistry import ProductRegistry

class User:
    def __init__(self, name):
        self.__name = name
        self.__products=ProductRegistry()
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def addProduct(self, product):
        error=self.__products.addProduct(product)
        if error is not None:
            return error
    def __str__(self):
        return f"User name {self.__name}"
    def getProducts(self):
        return self.__products.getSerializedProducts()
    def displayUserProducts(self):
        print(f"User {self.__name} has the following products:")
        products=self.__products.getProducts()
        for key in products:
            print(products[key])
    