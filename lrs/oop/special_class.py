# 定制类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __str__(self):
        return "Fib numbers %d" % 12

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a >= 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n): # 实现list[n]功能
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # 实现list的slice功能list[n:m]
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, item):  # 对象中没有该成员时的处理，有成员则不会调用该方法
        if item == "age":
            return lambda : 25
        raise AttributeError("Student has no attribue: %s" % item)


class UriChain(object):

    def __init__(self, path=""):
        self.__path = path

    def __getattr__(self, item):
        return UriChain("%s/%s" % (self.__path, item))

    def __str__(self):
        return self.__path

    __repr__ = __str__


if __name__ == "__main__":
    fib = Fib()
    print(fib)
    for n in fib:
        print(n)

    print(fib[5])
    print(fib[1:6])

    print(fib.age())  # () because return lambda function

    print(UriChain().user.id)
