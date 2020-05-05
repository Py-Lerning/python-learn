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
# 1.构造一个从3开始的生成器。这是一个无限序列。
def odd_generator():
    n = 1
    while True:
        n += 2
        yield n


# 2.定义一个筛选函数：
def not_divisible(n):
    return lambda x: x % n > 0


# 3.定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    ge = odd_generator()
    while True:
        n = next(ge)
        yield n
        ge = filter(not_divisible(n), ge)


# 判断是否是回文数字：常规写法
def is_palindrome1(n):
    start = 0
    end = len(str(n)) - 1
    while start < end:
        if (str[start] != str[end]):
            return False
        start = start + 1
        end = end - 1

    return True


# 判断是否是回文数字：进阶写法
def is_palindrome2(n):
    n = str(n)
    re = list(n)
    re.reverse()
    if list(n) == re:
        return True
    else:
        return False


# 判断是否是回文数字：大佬写法
def is_palindrome3(n):
    return str(n) == str(n)[::-1]


# 解释
# 字符串切片的表达式  s[开始:结束:步长]     步长通常是可以省略的
#
# 例如: s = 'abcd'
# -1 就是从后面开始，最后一个数字的下标：
# s[:-1]    跟  s[:-1:1] 和 s[:-1:]   相等，结果都是'abc'
#
# s[-1:]    跟 s[-1::1] 和 s[-1::]   相等，结果都是'd'
#
# 步长的意思，就是取值之间隔多少。
#
# 例如有一个序列 L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# L[::1] =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     (步长为1，意思就是截取数组下标相隔为1的元素，组成新序列)
#
# L[::2] = [0, 2, 4, 6, 8]   (步长为2，意思就是截取数组下标相隔为2的元素，组成新序列)
#
# 不懂这里为什么是倒着进行切片的。
# L[::-1]=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   (步长为-1， 意思反向截取，数组下标相隔为1的元素，组成新序列) why????
#
# L[2::-1] = [2, 1, 0]       (意思从数组下标为2的元素开始，反向截图数组下标相隔为1的元素，组成新序列)

if __name__ == "__main__":
    # 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()
    # 完成计算结果，需要用list()函数获得所有结果并返回list。
    print("光一个filter：%s " % filter(odd, [1, 2, 4, 5, 6, 9, 10, 15]))
    print("用list包装一下：%s " % list(filter(odd, [1, 2, 4, 5, 6, 9, 10, 15])))

    print(list(filter(delete_empty, ["1", ""])))

    print("----")
    ge = odd_generator()
    ge = filter(not_divisible(3), ge)
    print(next(ge))

    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(L[2::-1])
