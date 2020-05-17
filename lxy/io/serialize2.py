#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pickle

import unittest

from lxy.err_learn.dict_test import Dict


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    # 错误的原因是Student对象不是一个可序列化为JSON的对象。
    def test_dump_class_instance(self):
        s = Student('Bob', 20, 88)
        with self.assertRaises(BaseException):
            print(json.dumps(s))

    # 必须要手写一个方法，才可以完成转换。告诉json.dump，如何把我们的student进行转换
    # 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
    def test_dump_with_default(self):
        s = Student('Bob', 20, 88)
        print(json.dumps(s, default=student2dict))

    # 我们可以偷个懒，把任意class的实例变为dict：
    # 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
    def test_dump_with_class_dict(self):
        s = Student('Bob', 20, 88)
        print(json.dumps(s, default=student2dict))

    def test_load_with_object_hook(self):
        json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        print(json.loads(json_str, object_hook=dict2student))

if __name__ == "__main__":
    # 这样就可以把mydict_test.py当做正常的python脚本运行：
    unittest.main()

    # 另一种方法是在命令行通过参数 - m unittest直接运行单元测试：
    # python -m unittest mydict_test
