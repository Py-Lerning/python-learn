#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap
import os, argparse

# 一、namedtuple
def namedtuple_learn():
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
    Point = namedtuple('Point', ['x', 'y'])
    # 直接调用会报错。TypeError: __new__() missing 2 required positional arguments: 'x' and 'y'
    # p = Point()

    p = Point("harry", "potter");
    print(p)

    # 不能这样写，只能当做一个list把参数传递进去
    # p1 = Point(x = 123,y = 23)

    p2 = Point(1, 2)
    print(p2.x)
    print(p2.y)

    print(isinstance(p, Point))
    print(isinstance(p, tuple))


# 二、deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
def deque_learn():
    q = deque(['a', 'b', 'c'])
    # 从队列的末尾添加的

    q.append("d")
    print(q)
    q.pop()
    print(q)

    # 从队列的头部添加的
    q.appendleft('y')
    print(q)

    q.popleft()
    print(q)


# 三、defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
def defaultdict_learn():
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])

    print(dd['key2'])

    d2 = {"key1": 'abc'}
    print(d2['key1'])

    # 下面就直接报错了：KeyError: 'key2'
    # print(d2['key2'])


# 四、OrderedDict
def OrderedDict_learn():
    od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
    # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
    print(list(od.keys()))  # 按照插入的Key的顺序返回


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    # 【文章：】[Python __setitem__()、__getitem__()、__delitem__()](https://www.cnblogs.com/royfans/p/8191253.html)
    # __xxxitem__:使用 [''] 的方式操作属性时被调用
    #
    # __setitem__:每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
    #
    # __getitem__:当访问不存在的属性时会调用该方法
    #
    # __delitem__:当删除属性时调用该方法
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        # print(len(self))
        # 如果每次dict的len已经超过了_capacity，那就要对应删除掉一个item了
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# 五、ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# [关于ChainMap 的讨论](https://www.liaoxuefeng.com/discuss/969955749132672/1294491747090466)
# [Python面向对象中super用法与MRO机制](https://www.cnblogs.com/chenhuabin/p/10058594.html)


if __name__ == "__main__":
    # deque_learn()
    # defaultdict_learn()
    # OrderedDict_learn()
    #
    # d = LastUpdatedOrderedDict(2)
    # d["key1"] = "abc"
    # d["key2"] = "abc2"
    # d['key3'] = 'abc3'

    defaults = {'color': 'red', 'user': 'guest'}  # 默认参数-字典

    parser = argparse.ArgumentParser()  # 参数解析器，不懂的暂时也不用去管了
    parser.add_argument('-u', '--user')  # 配置解析器，
    parser.add_argument('-c', '--color')  # 同上，↑记住 ’-u‘ 这两个字符就ok
    namespace = parser.parse_args()  # 运行解析器了

    command_line_args = {k: v for k, v in vars(namespace).items() if v}  # 命令行参数-字典
    # 将解析器分成了无数个小部分并用字典生成器重做成一个保存有解析器信息的字典
    # { k: v for k, v in vars(namespace).items() if v }是字典生成器
    # vars(namespace).items() #vars获取namespace解析器属性并以dict形式返回，items()将dict转为list

    # 构造命令行参数:在命令行中这样执行： python3  collections_learn.py -u bob
    # user=admin color=green python3 collections_learn.py -u bob
    combined = ChainMap(command_line_args, os.environ, defaults)  # 绑着三个字典的“大字典”
    # 用ChainMap 链接3字典，分别是：命令行参数-字典、环境变量参数-字典、默认参数-字典
    # 命令行参数-字典 在最前位置具有最高优先级，默认参数-字典 优先级最低

    print('color=%s' % combined['color'])  # 打印大字典combined['color']对应的value
    print('user=%s' % combined['user'])  # 打印......
    # 按优先级查找combined['color']...最先在命令行参数-字典里查找对应的key，没有找到...再在环境变量里找，还没找到...最后去默认参数里找，找到了！打印defaults['color']

    # 命令行参数、环境变量可以且只能在cmd里添加的...这一节只是讲ChainMap的拓展用法，实际上很少用到不清楚也没事
