
class classeB:
    testVar = ''

    def __init__(self, x=5, y=6):
        self.x=x
        self.y=6

    def contaVarClasse(self, t, n):
        counter = 0
        for i, item in enumerate(classeB.__mro__):
            if i > n-1:
                break
            else:
                try:
                    for key, value in vars(item).items():
                        if type(value) == t and key != '__module__' and key != '__doc__':
                            counter += 1
                except:
                    print("Error")

        print(counter)

"""def contaVarClasse(self, mytype, n):
    count = 0
    for num,classe in enumerate(type(self).mro(), start=1):
        for k in vars(classe).items():
            if isinstance(k, mytype):
                count = count + 1 
    
        if num==n: return count
    return count"""