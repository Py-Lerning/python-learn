#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 定义了一个字典
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print("%s" % d)

    # 更新value
    d['Adam'] = 67
    print("更新value：%s" % d)

    # 如果key不存在，dict就会报错：
    # print("如果key不存在，dict就会报错：%s" % d['Thomas'])

    # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
    print("通过in判断是否存在：%s" % 'Thomas' in d)

    # 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
    print("通过dict提供的get()：%s" % d.get('Thomas'))

    # 要删除一个key，用pop(key)方法
    d.pop('Bob')
    print("要删除一个key：%s" % d)

    # 定义了一个集合
    s = set([1, 2, 3])
    print("定义了一个集合:%s" % s)

    # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
    s.add(4)
    print("通过add添加元素:%s" % s)

    # 通过remove(key)方法可以删除元素：
    s.remove(4)
    print("通过remove删除元素:%s" % s)

    # 两个set可以做数学意义上的交集、并集等操作
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print("交集:%s" % (s1 & s2))
    print("并集:%s" % (s1 | s2))