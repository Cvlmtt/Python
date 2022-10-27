@staticmethod
def present(list, x):
    for i in list:
        if i == x:
            return True
    return False

@staticmethod
def permutation(l):
    dic = l.copy()
    res = list()
    queue = list()
    for i in l:
        t = list()
        t.append(i)
        queue.append(t)


    while len(queue) != 0:
        x = queue.pop(0)
        if len(x) == len(l):
            res.append(x)
        else:
            for i in dic:
                if i not in x:
                    temp = x.copy()
                    temp.append(i)
                    queue.append(temp)
    return res


lis = [1, 2, 3, 4]

res = permutation(lis)

print(res)
print(len(res))
