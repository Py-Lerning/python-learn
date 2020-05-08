#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


if __name__ == "__main__":
    s = Student()  # 创建新的实例
    s.name = 'Michael'  # 绑定属性'name'
    s.score = 99  # 绑定属性'score'。报错
