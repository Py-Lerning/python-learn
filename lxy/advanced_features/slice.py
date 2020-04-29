#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
    if len(L) != 0:
        max = L[0]
        min = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return (min, max)
    return (None, None)


if __name__ == "__main__":
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    # 从下标1开始，不包括2
    l1 = L[1:2]

    print("原先：%s 和切片切出来的：%s" % (L, l1))

    # 切片是复制，操作切片和原始值没有影响
    l1.append("harry")
    print("添加元素后原先：%s 和切片切出来的：%s" % (L, l1))

    # 既然Python支持L[-1]
    # 取倒数第一个元素，那么它同样支持倒数切片
    # 记住倒数第一个元素的索引是 - 1。

    # tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
    t = (0, 1, 2, 3, 4, 5)[:3]
    print(t)

    # 切出来的继续切
    t[1:2]
    print(t)

    # 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
    # Python没有针对字符串的截取函数，只需要切片一个操作就可以完成
