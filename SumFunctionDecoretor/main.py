import functools


def decora(function):
    @functools.wraps(function)
    def wrapper(lst):
        args = []
        for i in lst:
            try:
                x = int(float(i))
                args.append(x)
            except:
                pass
        return function(*args)
    return wrapper


@decora
def somma(*args, **kwargs):
    if len(args)+len(kwargs) < 2:
        raise Exception("ERROR: number of elements less then 2")
    sum = 0
    for arg in args:
        sum += arg
    for key, value in kwargs.items():
        sum += value
    return sum


res = somma([1, 5.3, "10.5", "diomerda"])
print(res)