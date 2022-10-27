from MyClass import MyClass


class MyProxy:
    def __init__(self, x):
        self.__MyClass = MyClass(x)

    def __getattr__(self, item):
        return self.__MyClass.__getattribute__(item)