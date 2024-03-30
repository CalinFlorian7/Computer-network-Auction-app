

class User:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"Name: {self.__name}"
    