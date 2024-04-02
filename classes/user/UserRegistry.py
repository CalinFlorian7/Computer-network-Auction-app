

class UserRegistry:
    __users={}
    # _instance=None
    def __init__(self):
        self.__users={}
    # @staticmethod
    # def getInstance():
    #     if UserRegistry._instance==None:
    #         UserRegistry._instance=UserRegistry()
    #     return UserRegistry._instance
    def getUsers(self):
        return self.__users
    def addUser(self,user):
        if user.get_name() not in self.__users:
            self.__users[user.get_name()]=user
    def userNameExists(self,userName):
        if userName in self.__users:
            return True
        else:
            return False
    def addProductForUser(self,userName,product):
        if userName in self.__users:
            self.__users[userName].addProduct(product)
        else:
            print(f"User {userName} does not exist")
    def updateProductFinalPrice(self,productName,updatedPrice):
        for userName in self.__users:
            userCurent=self.__users[userName]
            products=userCurent.getProducts()
    
            if productName in products:
                if (products[productName].getStartingPrice())>= updatedPrice:
                    print(f"Price {updatedPrice} is lower than the starting price {products[productName].getStartingPrice()}")
                elif (products[productName].getFinalPrice())>= updatedPrice:
                    print(f"Price {updatedPrice} is lower than the final price {products[productName].getFinalPrice()}")
                else:

                     products[productName].setFinalPrice(updatedPrice)
            else:
                print(f"Product {productName} does not exist for user {userName}")
            
    def displayUsers(self):
        print("Users already added:")
        for userName in self.__users:
            userCurent=self.__users[userName]
            print(userCurent.__str__())
            for product in userCurent.getProducts():
                print(product)
            
        #   print(f"User name{user.get_name()} Starting Price{user.get_startingPrice()} Final price {user.get_finalPrice()}")    