#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique

import logging

def main():
    try:
        r = 10/0
    except Exception as e:
        logging.exception(e)


# 手动定义一个错误类型，继承自ValueError，然后用raise关键字抛出
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')

        # raise语句如果不带参数，就会把当前错误原样抛出。
        # 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
        raise
        # raise ValueError('input error!')


def func():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    # Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
    # 所以就和java中的Exception一样
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('except:', e)

    # 没有错误就执行这个else
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')


if __name__ == "__main__":
    # func()

    # main()

    bar()