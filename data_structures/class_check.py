class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

@profile
def func():
    res = [Point(2*i, 3*i) for i in xrange(10000)]
    return res

if __name__ == '__main__':
    res = func()

