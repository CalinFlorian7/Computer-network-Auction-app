
class Product:
    
    def __init__(self, name, startingPrice):
        self.__name = name
        self.__startingPrice = startingPrice
        self.__finalPrice = startingPrice
    

    def getFinalPrice(self):
        return self.__finalPrice
    def setFinalPrice(self, finalPrice):
        self.__finalPrice = finalPrice

    def getStartingPrice(self):
        return self.__startingPrice
    def setStartingPrice(self, startingPrice):
        self.__startingPrice = startingPrice
    def serialize(self):
        return {"name":self.__name,"startingPrice":self.__startingPrice,"finalPrice":self.__finalPrice}
    @staticmethod
    def deserialize(data):
        return Product(data["name"],data["startingPrice"])

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name   
    def __str__(self):
        return f"Name: {self.__name} Starting Price:  {str(self.__startingPrice)} Final Price: {str(self.__finalPrice)}"
    