#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

# 1.map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
from functools import reduce


def f(x):
    return x * x


# 2.reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': [3, 3], '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '12': 222}


def fn(x, y):
    return x * 10 + y


def getint(s1):
    return DIGITS[s1]


def f1(x, y):
    return x * 10 + y


def f2(a, b):
    return a / 10 + b


def str2ints(s):
    return reduce(fn, map(getint, s))


def normalize(name):
    name = name.lower()
    return name[0].upper() + name[1:]


def prod(L):
    return reduce(lambda x, y: x * y, L)


def str2float(s):
    L = list(s)
    i = L.index('.')
    L1, L2 = L[:i], L[i + 1:]
    L2.reverse()
    return reduce(f1, map(f, L1)) + reduce(f2, map(f, L2)) / 10


if __name__ == "__main__":
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(r)  # <map object at 0x10a8d3090>
    print(list(r))

    # reduce 产生的东西
    print(reduce(fn, [1, 3, 5, 7, 9]))

    # map 产生的结果是一个map对象
    print(map(getint, "2"))
    print(map(getint, "3"))
    print(list(map(getint, "12")))

    print("str2ints----")
    # 结果：[3, 3]。通过debug发现，如果是光一个参数3，通过DIGITS得到的结果是[3,3]，然后reduce函数就没再走了。
    # 大概理解reduce函数是要接受两个参数的，如果只有一个参数。java里面会提供一个默认值，用这个默认值和这个参数进行运算。python里面没有默认值
    print("输入2，结果：%s" % str2ints("3"))

    # 下面会报错
    # print("输入234，结果：%s" % str2ints("234"))

    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
