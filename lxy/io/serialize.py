#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


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
        print(globals())    # 返回全局变量的字典。
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

    s = json.loads(text, object_hook=json2object)

    print(s.name)
    print(s.age)
    print(s.score)