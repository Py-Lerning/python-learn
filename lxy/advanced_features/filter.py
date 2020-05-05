#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 1.和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数
def odd(n):
    return n % 2 != 0


# 把一个序列中的空字符串删掉
def delete_empty(s):
    # return s != None and s != ''
    return s and s.strip()

# 用filter求素数
# 1.构造一个从3开始的生成器
if __name__ == "__main__":
    # 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()
    # 完成计算结果，需要用list()函数获得所有结果并返回list。
    print("光一个filter：%s " % filter(odd, [1, 2, 4, 5, 6, 9, 10, 15]))
    print("用list包装一下：%s " % list(filter(odd, [1, 2, 4, 5, 6, 9, 10, 15])))

    print(list(filter(delete_empty, ["1", ""])))
