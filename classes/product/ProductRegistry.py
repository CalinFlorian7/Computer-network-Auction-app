
from classes.product.Product import Product
class ProductRegistry:
    __products = {}
    # _instance=None
    
    def __init__(self):
        self.__products = {}
    # @staticmethod
    # def getInstance():
    #     if ProductRegistry._instance==None:
    #         ProductRegistry._instance=ProductRegistry()
            
    #     return ProductRegistry._instance
    def getProducts(self):
        return self.__products
    def getSerializedProducts(self):
        products={}
        for productName in self.__products.keys():
            product=self.__products[productName]
            products[productName]=product.serialize()
        return products
    def addProduct(self,product):
        if product.getName() not in self.__products:
            self.__products[product.getName()] = product
        else:
            return "This product already exists"
    def serialize(self):
        products={}
        for productName in self.__products.keys():
            product=self.__products[productName]
            products[productName]=product.serialize()
    @staticmethod
    def deserialize(data):
        products={}
        for productName in data.keys():
            product=Product.deserialize(data[productName])
            products[productName]=product
        return products
    
           
   
    def productNameExists(self,productName):
        if productName in self.__products:
            return True
        else:
            return False
    def displayProducts(self):
        print("Products already added:")
        for productName in self.__products:
            produsCurent=self.__products[productName]
            print(produsCurent.__str__())
        #   print(f"Product name{product.get_name()} Starting Price{product.get_startingPrice()} Final price {product.get_finalPrice()}")
        