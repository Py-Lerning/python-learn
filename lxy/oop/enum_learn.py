#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    # Sun = 0 # Sun的value被设定为0
    Mon = 8
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == "__main__":
    # value属性则是自动赋给成员的int常量，默认从1开始计数。
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    # 访问
    print(Weekday.Mon)
    print(Weekday["Mon"])
    print(Weekday["Mon"].value)

    # 如果根据value去获取的时候，不在枚举类定义的范围内，则直接报错
    # print(Weekday(1))
    # print(Weekday(7))
