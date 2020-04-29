#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def my_abs(x):
    # 参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
    if not isinstance(x, (int, float)):
        raise TypeError("参数类型异常")
    if x >= 0:
        return x
    else:
        return -x


# 如果想定义一个什么事也不做的空函数，可以用pass语句：起到占位符的作用
def nop():
    pass


# 返回多个值
# 返回值是一个tuple，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# python的函数可以有以下几种：必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# 默认参数
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 定义默认参数的坑
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=[]):
    L.append('END')
    return L


# 修正：可以用None来代替
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数：
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 关键字参数：
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数：
# 通过*进行分割，要求必须传入这些参数。如果没有传入参数名，调用将报错：
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)

if __name__ == "__main__":
    res = my_abs(-1)
    print("my_abs：%s" % res)

    # res = my_abs("A")
    # print("my_abs参数类型异常：%s" % res)

    res = move(1, 2, 3)
    # 返回的是一个元组，但是元组是不能被这样格式化的
    # print("move返回的1个值：%s " % res)
    print(res)

    x, y = move(1, 2, 3)
    print("move返回的多个值：x:%s,y:%s " % (x, y))

    L = add_end()  # ['END']
    print("第一次调用add_end:%s " % L)

    L = add_end()  # ['END', 'END']
    print("第二次调用add_end:%s " % L)

    L = add_end()  # ['END', 'END', 'END']
    print("第三次调用add_end:%s " % L)

    i = calc(1, 2)
    print("直接调用可变参数的函数:%s " % i)

    nums = [1, 2, 3]
    i = calc(*nums)
    print("使用现有的list，直接调用可变参数的函数:%s " % i)

    tup = (1, 2, 3)
    i = calc(*tup)
    print("使用现有的tuple，直接调用可变参数的函数:%s " % i)

    # 调用关键字参数
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=extra['city'], job=extra['job'])
    person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

    # ** extra表示把extra这个dict的所有key - value用关键字参数传入到函数的 ** kw参数，
    # kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
    person('Jack', 24, **extra)
