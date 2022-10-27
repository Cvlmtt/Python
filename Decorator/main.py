import functools


def decf(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) != 2:
            raise TypeError
        else:
            res = func(*args, **kwargs)
            f = open("risultato.txt", 'a')
            if res is not None:
                f.write(str(res))
            if args:
                f.write(str(args[0]))
            else:
                f.write(str(next(iter(kwargs.values()))))
            f.write("\n")
            f.close()
            return res
    return wrapper

@decf
def foo(first, second):
    return first + second


print(foo(2, 3))