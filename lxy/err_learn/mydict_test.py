#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import Any

from lxy.err_learn.unit_test import Dict


# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()

        # 这种方式，调用一下 __setattr__ 方法
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            # d['empty']就是dict用法。如果没有这个属性就直接报错 KeyError
            value = d['empty']

    # 通过d.empty访问不存在的key时，我们期待抛出AttributeError：
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            # d.empty就是object用法。如果没有属性，就走我们自定义的 __getattr__
            value = d.empty

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

if __name__ == "__main__":
    # 这样就可以把mydict_test.py当做正常的python脚本运行：
    unittest.main()

    # 另一种方法是在命令行通过参数 - m unittest直接运行单元测试：
    # python -m unittest mydict_test