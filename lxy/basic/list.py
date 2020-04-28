#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 定义一个列表
    classmates = ['Michael', 'Bob', 'Tracy']
    print("定义一个列表：%s" % classmates)

    # 获取列表长度
    print("列表长度：%s" % len(classmates))

    # 用下标访问每个元素，正数下标
    print("访问第一个元素，下标：%d 值：%s" % (0, classmates[0]))

    # 用下标访问每个元素，正数下标。和java的数组一样，超过了就会报错：IndexError: list index out of range
    # print("访问第一个元素，下标：%d 值：%s" % (3, classmates[3]))

    # 用下标访问每个元素，负数下标
    print("访问第一个元素，下标：%d 值：%s" % (-1, classmates[-1]))

    # 追加元素到末尾
    classmates.append('Adam')
    print("追加元素到末尾：%s" % classmates)

    # 把元素插入到指定的位置
    classmates.insert(1, 'Jack')
    print("把元素插入到指定的位置：%s" % classmates)

    # 要删除list末尾的元素
    classmates.pop()
    print("要删除list末尾的元素：%s" % classmates)

    # 要删除指定位置的元素
    classmates.pop(1)
    print("要删除指定位置的元素：%s" % classmates)

    # 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
    classmates[1] = 'Sarah'
    print("直接赋值元素下标：%s" % classmates)

    # list元素也可以是另一个list
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print("list元素也可以是另一个list：%s" % s)