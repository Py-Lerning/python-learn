#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]

# 再按成绩从高到低排序：
def by_score(t):
    return t[1]


if __name__ == "__main__":
    # 1.Python内置的sorted()函数就可以对list进行排序：
    print(sorted([36, 5, -12, 9, -21]))

    # 2.此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
    # key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
    print(sorted([36, 5, -12, 9, -21], key=abs))

    # 3.默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
    print(sorted(['bob', 'about', 'Zoo', 'Credit']))

    # 4.我们给sorted传入key函数，即可实现忽略大小写的排序：
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

    # 5.要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

    L2 = sorted(L, key=by_name)
    print(L2)

    L2 = sorted(L, key=by_score)
    print(L2)
