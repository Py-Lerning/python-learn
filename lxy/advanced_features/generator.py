#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(n):
    count = 0
    x1 = 0
    x2 = 1
    while count < n:
        print(x2)
        x1, x2 = x2, x1 + x2
        count = count + 1


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 参考评论区大神写法
def triangles():
    res = [1]
    while True:
        res = [res[0]] + [res[x] + res[x + 1] for x in range(len(res) - 1)] + [res[0]]
        yield res


if __name__ == "__main__":
    # 列表生成式创建一个list
    L = [x * x for x in range(10)]

    # 创建一个generator1：
    g = (x * x for x in range(10))

    # 通过next()函数获得generator的下一个返回值：（调用到最后没有元素会报错）
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

    # 使用for循环，因为generator也是可迭代对象
    for n in g:
        print(n)

    # 报错
    # next(g)

    # generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
    fib(5)

    # fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
    f = fib2(3)
    print("----")
    print(next(f))
    print(next(f))
    print(next(f))

    # 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
    while True:
        try:
            # 这个生成器一共产生3个值，已经调用过3次next，下一次就会报错
            x = next(f)
            print('f:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
        break

    # 这样是不会把1算上的
    for x in range(1):
        print(x)

    t = triangles()
    print(next(t))
    print(next(t))
    print(next(t))
    print(next(t))
