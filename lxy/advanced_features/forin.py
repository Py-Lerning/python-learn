#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

if __name__ == "__main__":
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    # 迭代方式1：
    for key in L:
        print("迭代：", key)

    # 迭代方式2：有下标
    for i, value in enumerate(L):
        print("迭代：下标：%i , value:%s" % (i, key))

    # 判断是否可以进行迭代
    instance1 = isinstance(L, Iterable)
    print("list L是否可以进行迭代：", instance1)

    instance1 = isinstance(123, Iterable)
    print("整数是否可以进行迭代：", instance1)

    # 迭代字典1：
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    for key in dict1:
        print("迭代字典key：", key)

    # 迭代字典：这样是不行的
    # for key, value in dict1:
    for k, v in dict1.items():
        print("迭代字典key：%s ，value：%s" % (k, v))

    # 同时引用了两个变量
    for x, y in ((1, 1), (2, 2)):
        print("迭代元组,x:%s ,y:%s" % (x, y))


    L2 = [x.lower() for x in L1 if isinstance(x, str)]
