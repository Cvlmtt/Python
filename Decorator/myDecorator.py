import functools
from functools import wraps


def myDecorator(aClass):
    def contaVarClasse(self, t):
        counter = 0
        dict = type(self).__dict__
        for key in dict:
            if key != '__module__' and key != '__doc__':
                if type(dict[key]) == t:
                    counter += 1
        print(counter)

    aClass.varCountClass = contaVarClasse
    return aClass


@myDecorator
class Test:
    c = 1

    def __init__(self):
        print("ciao")


x = Test()
x.varCountClass(int)


class classeBase:
    varC = 1000

    def __init__(self):
        self.varL = 10

    def f(self, v):
        print(v * self.varL)

    @staticmethod
    def g(x):
        print(x * __class__.varC)

def extendBaseClass(Class):
    setattr(Class, "varC", classeBase.varC)
    setattr(Class, "__init__", classeBase.__init__)
    setattr(Class, "f", classeBase.f)
    setattr(Class, "g", classeBase.g)
    return Class

@extendBaseClass
class Figlio:
    pass

print("New exercise")
f = Figlio()
print(f.varC)
f.f(3)
Figlio.g(5)