class MyDictionary:
    class MyPair:
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def setValue(self, v):
            self.value = v

        def setKey(self, k):
            self.key = k

    def __init__(self):
         self._L = list()

    def __getitem__(self, key):
        if not self.isEmpty():
            for i in self._L:
                if key == i.getKey():
                    return i.getValue()
            return None
        return None

    def __setitem__(self, key, value):
        if key in self:
            for i in self._L:
                if key == i.getKey():
                    i.setValue(value)
        else:
            self._L.append(MyDictionary.MyPair(key, value))

    def __delitem__(self, key):
        if key in self:
            for i, item in enumerate(self._L):
                if key == item.getKey():
                    self._L.pop(i)

    def __len__(self):
        return len(self._L)

    def isEmpty(self):
        if len(self) == 0:
            return True
        return False

    def __contains__(self, key):
        if not self.isEmpty():
            for i in self._L:
                if key == i.getKey():
                    return True
            return False
        else:
            return False

    def __eq__(self, other):
        if self.isEmpty() and other.isEmpty():
            return True
        elif len(self) == len(other):
            for i in self._L:
                for j in other._L:
                    if i.getKey() == j.getKey() and i.getValue() == j.getValue():
                        break
                else:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        if self.isEmpty() and other.isEmpty():
            return False
        elif len(self) == len(other):
            for i in self._L:
                for j in other._L:
                    if i.getKey() == j.getKey() and i.getValue() == j.getValue():
                        break
                else:
                    return True
            return False
        else:
            return True

    