#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 你可以使用issubclass()或者isinstance()方法来检测。

# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。


# 基础重载方法：

# 1	__init__ ( self [,args...] )
# 构造函数
# 简单的调用方法: obj = className(args)

# 2	__del__( self )
# 析构方法, 删除一个对象
# 简单的调用方法 : del obj

# 3	__repr__( self )
# 转化为供解释器读取的形式
# 简单的调用方法 : repr(obj)

# 4	__str__( self )
# 用于将值转化为适于人阅读的形式
# 简单的调用方法 : str(obj)

# 5	__cmp__ ( self, x )
# 对象比较
# 简单的调用方法 : cmp(obj, x)

class Animal(object):
    def run(self):
        print('Animal is running...')

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。【多态。】
class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


# 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

# 【静态语言 vs 动态语言】
# 1.对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 2.对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')

def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == "__main__":
    a = Animal()
    a.run()
    print(isinstance(a, Animal))