

class AutoDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


a = AutoDict()
a[1][2] = 3
print(a[1][2])

