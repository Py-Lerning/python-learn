#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def python_dump():
    # 实例1    dumps()
    a = {'name': 'dream', 'age': '18'}
    a = json.dumps(a)  # dumps 加载进去

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

if __name__ == "__main__":
    python_load()