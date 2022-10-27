class Prova:
    def __init__(self, x):
        self.x = x

    def __setattr__(self, key, value):
        if key == "varA":
            super().__setattr__(key, value)
        elif key == "varB":
            super().__setattr__(key, value)
        else:
            setattr(Prova, key, value)

x = Prova(5)
print("before call __setattr__, used dir(): ", dir(Prova))
print("before call __setattr__, used vars(): ", vars(Prova))
x.pippo = "coca"
print("after call __setattr__, used dir(): ", dir(Prova))
print("after call __setattr__, used vars(): ", vars(Prova))
x.varA = "ciao"
print("after call __setattr__, used dir(): ", dir(Prova))
print("after call __setattr__, used vars(): ", vars(Prova))
print("after call __setattr__, used dir(): ", dir(x))
print("after call __setattr__, used vars(): ", vars(x))