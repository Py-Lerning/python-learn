#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pickle


# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 一、pickle模块
# 1.把一个对象序列化并写入文件。pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
def pickle_write_in_file1():
    d = dict(name='Bob', age=20, score=88)
    res = pickle.dumps(d)
    print(res)

    f = open("./pickle_write_in_file1", "wb")
    f.write(res)
    f.close()


def pickle_write_in_file2():
    d = dict(name='Bob', age=20, score=88)
    f = open("./pickle_write_in_file2", "wb")
    pickle.dump(d, f)
    f.close()


def pickle_read_from_file1():
    f = open('pickle_write_in_file1', 'rb')
    d = pickle.load(f)
    print(d)


def pickle_read_from_file2():
    f = open('pickle_write_in_file2', 'rb')
    s = f.read()
    d = pickle.loads(s)
    print(d)


# 二、json 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#

def json_dump():
    d = dict(name='Bob', age=20, score=88)
    # dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
    str = json.dumps(d)
    print(str)

    f = open('json_dump1', 'w')
    json.dump(d, f)

def json_load():
    f = open('json_dump1', 'r')
    load = json.load(f)
    print(load)
    print(type(load))

    f.seek(0,0)
    str = f.read()
    loads = json.loads(str)
    print(loads)
    print(type(loads))


def python_dump():
    # 实例1    dumps()
    a = {'name': 'dream', 'age': '18'}
    a = json.dumps(a)  # dumps 加载进去

    # dumps()方法返回一个str，内容就是标准的JSON。
    print(isinstance(a, str))  # True
    with open('json_test.json', 'w') as f:
        f.write(a)
        f.close()

    # 实例2    dump()
    a = {'name': 'dream', 'age': '18'}
    with open('json_test2.json', 'w') as f:
        json.dump(a, f)
        f.close()


def python_load():
    # 实例1    loads()
    with open('json_test.json', 'r') as f:
        a = f.read()
        a = json.loads(a)
        print(a['name'])  # dream
        f.close()
    # 实例2    load()
    with open('json_test2.json', 'r') as f:
        a = json.load(f)
        print(a['name'])  # dream
        f.close()


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


class Car(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def json2object(d):
    className = d.pop('__class__', None)
    if className:
        print(globals())  # 返回全局变量的字典。
        cls = globals()[className]
        return cls(**d)
    return d


text = '''
{
  "__class__": "Student",
  "name": "Bob",
  "age": 12,
  "score": 95
}
'''

if __name__ == "__main__":
    # python_load()

    # 传递一个json的str或者byte进去
    s = json.loads(text, object_hook=json2object)

    # 传递一个dic进去是不行的，会报错：TypeError: the JSON object must be str, bytes or bytearray, not 'dict'
    # text_dict = {"name": "harry"}
    # s = json.loads(text_dict, object_hook=json2object)

    print(s.name)
    print(s.age)
    print(s.score)

    # pickle_write_in_file1()
    # pickle_write_in_file2()
    #
    # pickle_read_from_file1()
    # pickle_read_from_file2()

    json_dump()
    json_load()
