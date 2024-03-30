
from classes.product.ProductRegistry import ProductRegistry

class User:
    def __init__(self, name):
        self.__name = name
        self.__products=ProductRegistry.getInstance()
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def add_product(self, product):
        self.__products.addProduct(product)
    def __str__(self):
        return f"User name {self.__name}"
    def displayUserProducts(self):
        print(f"User {self.__name} has the following products:")
        products=self.__products.getProducts()
        for key in products:
            print(products[key])
    