#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any


# 【文章：Python的__getattr__和__getattribute__】https://www.cnblogs.com/blackmatrix/p/5681480.html
# 总结：
# __getattr__
# __getattr__在当前主流的Python版本中都可用，重载__getattr__方法对类及其实例未定义的属性有效。也就属性是说，
# 如果访问的属性存在，就不会调用__getattr__方法。这个属性的存在，包括类属性和实例属性。

# __getattribute__
# __getattribute__仅在新式类中可用，重载__getattrbute__方法对类实例的每个属性访问都有效。

# 同时定义__getattribute__和__getattr__
# __getattr__方法不会再被调用，除非显示调用__getattr__方法或引发AttributeError异常。

# Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
            # print("遇到了异常")
            # raise

    def __setattr__(self, key, value):
        print("调用了一次set")
        self[key] = value


class Test:

    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

    # 报错，dict是不可以这样进行访问的：AttributeError: 'dict' object has no attribute 'name'
    # print("aaa", d.name)

    # 因为d没有name这个属性，就会直接报错。d["name"]是dict的用法，所以不经过__getattr__ 方法，直接报错：KeyError: 'name'
    # print(d["name"])

    d2 = Dict()

    # d2没有name这个属性，但是d2也是自定义的一个class，所以可以d.name进行访问。没有，就走到 __getattr__ 方法中
    # print(d2.name)

    t = Test()
    # 普通对象可以这样访问t.name，但是没有属性，就会报错。AttributeError: 'Test' object has no attribute 'name'
    # print(t.name)

    # 普通对象是不可以这么访问的：TypeError: 'Test' object is not subscriptable
    print(t["name"])

    '''
    getitem, setitem是序列,映射类型才有的, 比如字符串, 列表, 字典: getitem(key)方法用来访问个体元素。对序列类型，key只能是非负整数，对映射类型，关键字可以是任意Python不变对象。 setitem()方法给一个元素设定新值

__getattr__需要自己定义: 
1.访问一个类实例 x 的属性时，比如 x.a，解释器会先查找 x.__dict__["a"]，
2.若没有找到，则接着查询 x.__class__.__dict__["a"]，
3.如果还没找到，则按照上面提到的搜索顺序继续查询该类的父类们的名字空间，
4.如果还是没有找到，就要查看该类是否定义了__getattr__()方法，如果有这个方法就使用这个方法继续查找。
    '''
