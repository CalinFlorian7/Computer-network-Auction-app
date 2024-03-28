
class Product:
    
    def __init__(self, name, startingPrice,finalPrice):
        self.__name = name
        self.__startingPrice = startingPrice
        self.__finalPrice = finalPrice
    

    def get_finalPrice(self):
        return self.__finalPrice
    def set_finalPrice(self, finalPrice):
        self.__finalPrice = finalPrice

    def get_startingPrice(self):
        return self.__startingPrice
    def set_startingPrice(self, startingPrice):
        self.__startingPrice = startingPrice

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name   
    def __str__(self):
        return f"Name: {self.__name} Starting Price:  {str(self.__startingPrice)} Final Price: {str(self.__finalPrice)}"
    