#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

from lxy.oop.inherrit import Animal, Dog


def fn():
    pass


class MyObject(object):
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 1000

    def print(self):
        pass

if __name__ == "__main__":
    # 基本类型都可以用type()判断：
    print(type(123))

    # 如果一个变量指向函数或者类，也可以用type()判断：
    print(type(abs))

    # type()函数返回的是对应的Class类型
    if type('abc') == str:
        print("是字符串")

    # types 的内部属性
    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)

    # 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
    a = Animal()
    d = Dog()
    print(isinstance(a, Animal))
    print(isinstance(a, Dog))  # false
    print(isinstance(d, Dog))
    print(isinstance(d, Animal))

    # 能用type()判断的基本类型也可以用isinstance()判断：
    print(isinstance(123, int))

    # 还可以判断一个变量是否是某些类型中的一种
    isinstance([1, 2, 3], (list, str))

    o = MyObject()
    print(len(o))

    # 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
    print("----")
    print(hasattr(o, 'x'))
    print(getattr(o, "x"))
    print(setattr(o, "x", 19))  # None
    print(o.x)  # 19

    # 如果试图获取不存在的属性，会抛出AttributeError的错误：
    # print(getattr(o, "xx"))

    # 可以传入一个default参数，如果属性不存在，就返回默认值：
    print(getattr(o, "xx", 123))

    # 也可以获得对象的方法：
    print(hasattr(o, "print"))