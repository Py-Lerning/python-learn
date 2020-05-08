#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    # __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth


class Student1(object):
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    __slots__ = ('name', 'age', '_birth')  # 用tuple定义允许绑定的属性名称

    def __init__(self) -> None:
        self.name = ""

    # 类似于java中的toString() 方法

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 注意如果在交互式的terminal里面，直接打变量，显示的还是原来的东西。即便以及写了__str__方法。
    # 因为：直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
    # 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__ = __str__

    # 如果想被for...in...循环，就写这个方法。这个方法刚刚看了一下不是object里面的方法
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    # for...in...循环就是每次调用 __iter__ 方法返回的对象的next方法
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method() 来调用。能不能直接在实例本身上调用呢？
    # 在Python中，答案是肯定的。任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

    # __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
    def __call__(self):
        print('My name is %s.' % self.name)

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth


class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))


    def __call__(self, path):
        return Chain('%s/%s' % (self.__path, path))


    def __str__(self):
        return self.__path

    __repr__ = __str__

if __name__ == "__main__":
    # 【文章：】https: // www.liaoxuefeng.com / discuss / 969955749132672 / 1275471364878624
    # 这个解释真的很棒啊！综合了本节学的东西。应该单独抽出来作为一章进行练习
    print(Chain().users('michael').repos)  # /users/michael/repos

    s = Student()  # 创建新的实例
    s.name = 'Michael'  # 绑定属性'name'
    # s.score = 99  # 绑定属性'score'。报错

    # 没有赋值以前就get，直接报错。AttributeError: 'Student' object has no attribute '_birth'
    # print(s.birth)

    # 赋值以后再进行get就可以了（关闭了slot）
    s.birth = 99
    print(s.birth)

    # Student1 这个类，因为slot限制了只能有两个变量。一个name一个age。
    # 所以不管是在外部直接 s1.gender = 'male'还是调用setter方法 s1.birth = 99，都会报错。
    # 除非把slot去掉，或者在slot里面加上对应的属性
    s1 = Student1()
    s1.birth = 99

    # 验证 __str__ 方法
    print(s1)

    # 直接把对象当成方法来进行调用
    s1()

    # 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
    print(callable(max))
    print(s1)
    print(123)
