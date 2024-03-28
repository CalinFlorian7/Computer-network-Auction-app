

class ProductRegistry:
    __products = {}
    _instance=None
    
    def __init__(self):
        self.__products = {}
    @staticmethod
    def getInstance():
        if ProductRegistry._instance==None:
            ProductRegistry._instance=ProductRegistry()
            
        return ProductRegistry._instance
    def getProducts(self):
        return self.__products
    def addProduct(self,product):
        if product.get_name() not in self.__products:
            self.__products[product.get_name()] = product
    
           
   
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
        