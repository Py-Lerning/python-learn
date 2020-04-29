#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 定义一个元组，这个tuple不能变了，它也没有append()，insert()这样的方法
    classmates = ('Michael', 'Bob', 'Tracy')

    # 直接打印会报错：https://www.cnblogs.com/2bjiujiu/p/9062115.html
    # 原因：%s 表示把 value变量装换为字符串，然而value值是Python元组，Python中元组不能直接通过%s 和 % 对其格式化，则报错
    # print("定义一个元组：%s" % classmates)

    