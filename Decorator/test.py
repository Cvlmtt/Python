class test:
    x = 0
    def __init__(self, x):
        self.x = x
        print(vars(type(self)))
        for i in vars(type(self)):
            print(i,'n',type(i))

    def ciao(self):
        print("ciao")

x = test(5)
