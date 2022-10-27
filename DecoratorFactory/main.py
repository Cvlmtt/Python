def decora(classe, funz, ff):
    def dec(cls):
        setattr(cls, funz, getattr(classe, ff))
        return cls
    return  dec

class ClassConFF:
    def ff(self):
        print("DIOMERDA")

    def pippo(self):
        print("Diocane")

@decora(ClassConFF, "funz", "pippo")
class ClassTest:
    pass

x = ClassTest()
x.funz()