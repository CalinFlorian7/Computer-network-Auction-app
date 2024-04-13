

class UserRegistry:
    __users={}
    def __init__(self):
        self.__users={}
    def getUsers(self):
        return self.__users
    def addUser(self,user):
        if user.getName() not in self.__users:
            self.__users[user.getName()]=user
    def userNameExists(self,userName):
        if userName in self.__users:
            return True
        else:
            return False
    def addProductForUser(self,userName,product):
        if userName in self.__users:
           error= self.__users[userName].addProduct(product)
           if error is not None:
                return error
        else:
            print(f"User {userName} does not exist")
            
            
    def updateProductFinalPrice(self, userName, productName, updatedPrice):
                if userName in self.__users:
                    userCurrent = self.__users[userName]
                    products = userCurrent.getProducts()

                    if productName in products:
                        if products[productName].getStartingPrice() >= updatedPrice:
                            return f"Price {updatedPrice} is lower than the starting price {products[productName].getStartingPrice()}"
                        elif products[productName].getFinalPrice() >= updatedPrice:
                            return f"Price {updatedPrice} is lower than the final price {products[productName].getFinalPrice()}"
                        else:
                            products[productName].setFinalPrice(updatedPrice)
                    else:
                        return f"Product {productName} does not exist for user {userName}"
                else:
                    return f"User {userName} does not exist" 
    def getProductsForUser(self, userName):
        if userName in self.__users:
            userCurrent = self.__users[userName]
            return userCurrent.getProducts()
            return f"User {userName} does not exist" 
    def displayUsers(self):
        print("Users already added:")
        for userName in self.__users:
            userCurent=self.__users[userName]
            userCurent.displayUserProducts()