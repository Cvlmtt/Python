def decora(Class):
    Class.counter = 0
    oldInit = Class.__init__
    def __newInit__(self, *args, **kwargs):
        Class.counter += 1
        oldInit(self, *args, **kwargs)

    Class.__init__ = __newInit__
    return Class

@decora
class Test:
    pass

x = Test()
y = Test()

print(Test.counter)