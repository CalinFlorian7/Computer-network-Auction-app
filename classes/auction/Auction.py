import classes
Product=classes.Product

class Auction:
        
        def __init__(self, userName,product):
            self.__product = Product(product.get_name(),product.getStartingPrice())
            self.__owner = userName
            self.__bids = {}
        
        def getOwner(self):
            return self.__owner
        def getLastBid(self):
            if len(self.__bids)==0:
                return None
            return self.__bids[max(self.__bids)]
        def getProduct(self):
            return f"Product {self.__product.getName()} with starting price {self.__product.getStartingPrice()} and current price {self.__product.getFinalPrice()}"
        def bid(self,bidPrice,bidderName):
            if bidPrice>self.__product.getFinalPrice():
                self.__product.setFinalPrice(bidPrice)
                self.__bids[bidPrice]=bidderName
                return None
            return "Bid price is lower than current price"