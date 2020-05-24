#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 关于两个内建函数 [Python入门基础知识(1) :locals() 和globals()](https://www.cnblogs.com/wanxsb/archive/2013/05/07/3064783.html)
class My():
    'Test'

    def __init__(self, name):
        self.name = name

    def test(self):
        print(self.name)


if __name__ == "__main__":
    # {'__module__': '__main__', '__doc__': 'Test', '__init__': <function My.__init__ at 0x1041c5a60>, 'test': <function My.test at 0x1041c5ae8>, '__dict__': <attribute '__dict__' of 'My' objects>, '__weakref__': <attribute '__weakref__' of 'My' objects>}
    print(vars(My))  # 返回一个字典对象，他的功能其实和  My.__dict__  很像)
    print(My.__dict__)

    harry = My("harry")
    print(vars(harry))  # {'name': 'harry'}
    print(harry.__dict__) # {'name': 'harry'}
