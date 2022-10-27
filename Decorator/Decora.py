import functools


def decora(foo):
    @functools.wraps(foo)
    def wrapper(*args, **kwargs):
        result = ''
        if len(kwargs) == 0:
            for arg in args:
                if type(arg) != str:
                    raise TypeError
                else:
                    result += arg + ' '
            res = foo(*args, **kwargs)
            result += str(res)
            return result
        else:
            raise TypeError

    return wrapper
    """out = ""
    #for arg in chain((args), wkargs, value())
    for arg in list(args)+[v for k, v in kwargs.item()]:
        if type(arg)!=str:
            raise TypeError
        out += arg+" "
    result = str(f(*args, **kwargs))
    out += result
    return out"""

@decora
def func(*args):
    counter = 0
    for arg in args:
        counter += 1
    return counter


print(func("ciao", "mondo", "sono"))
