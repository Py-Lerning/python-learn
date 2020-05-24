#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文章：[Python面向对象中super用法与MRO机制](https://www.cnblogs.com/chenhuabin/p/10058594.html)
class A(object):
    def fun(self):
        print('A.fun')

class B(object):
    def fun(self):
        print('B.fun')

class C(object):
    def fun(self):
        print('C.fun')

class D(A,B):
    def fun(self):
        print('D.fun')

class E(B, C):
    def fun(self):
        print('E.fun')

class F(D, E):
    def fun(self):
        print('F.fun')



class A1:
    def fun(self):
        print('A.fun')

class B1(A1):
    def fun(self):
        super(B1 , self).fun()
        print('B.fun')

class C1(A1):
    def fun(self):
        super(C1 , self).fun()
        print('C.fun')

class D1(B1 , C1):
    def fun(self):
        super(D1 , self).fun()
        print('D.fun')



if __name__ == "__main__":
    # [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
    # F->D->A->E->B->C->object
    print(F.mro())

    # 1.关于 super(type , obj)
    # super会按照__mro__属性中的顺序去查找方法，super(type , obj)两个参数中type作用是定义在__mro__数组中的那个位置开始找，obj定义的是用哪个类的__mro__元素。
    super(E, F()).fun()  # 输出结果：B.fun
    super(D, F()).fun()  # 输出结果：A.fun
    super(F, F()).fun()  # 输出结果：D.fun
    # F的mro顺序：调用的都是type对应的类在__mro__顺序中的下一个类的fun方法。
    #     调用的都是type对应的类在__mro__顺序中的下一个类的fun方法。


#     再让type保持不变，obj尝试不同的实例：
#     [<class '__main__.B'>, <class 'object'>]
    print(B.mro())

    super(B , F()).fun() # 输出结果：C.fun
    super(B , E()).fun() # 输出结果：C.fun
    # super(B , B()).fun() # 这是错误的，会报错：AttributeError: 'super' object has no attribute 'fun'

    print("-------")
    # 结果：A.fun
    # C.fun
    # B.fun
    # D.fun
    D1().fun()

    # 解释：来解释一下为什么输出顺序是A->C->B->D。
    # 首先我们要明白，D类的__mro__顺序是D->B->C->A，
    # 在D类中调用fun方法，然后在D类fun方法中遇到super(D , self).fun()，这个self指的是D类的实例化对象，所以用的是D类的__mro__顺序，而且指明位置是D后面也就是B类，所以继续调用B类的fun方法，
    # 遇到super(B , self).fun()，这时候需要注意，这里的self还是原来的D类实例（千万注意不是B类实例），所以还是用D类的__mro__顺序，
    # 那就继续调用下一个C类的fun方法，同理继续调用下一个父类，也就是A类的fun方法，
    # 执行完A类的fun方法后，回到C的fun方法中，打印输出，然后回到B类的fun方法，知道D类的fun方法打印输出完。