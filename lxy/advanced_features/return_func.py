#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 这一节的内容：https://www.liaoxuefeng.com/wiki/1016959663602400/1017434209254976

# 闭包

# 局部变量和全局变量：
# 【文章：】https://blog.csdn.net/zsdxqsjxlomer/article/details/78381626?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3
# 【总结：】
# 因为python是弱类型语言，赋值语句和其定义变量的语句一样，所以a=[4,5,6]'这句中，它是“有歧义的“，因为它既可以是表示
# 1.引用全局变量a，也可以是创建一个新的局部变量，所以在python中，默认它的行为是创建局部变量，除非显式声明global，
# 2.global定义的本地变量会变成其对应全局变量的一个别名，即是同一个变量。

# 什么样的情况下，list和dict不用global呢？
# 1.当在函数内是用list或dict的内置函数进行修改时，如append、remove等方法，
# 2.而非‘=’赋值时，可以不用global声明

# 【文章：】https://blog.csdn.net/bigxuyang/article/details/77877935
# 【总结：】可变数据类型
# 1.可变数据类型，值可以改变：列表list和字典dict；
# 2.不可变数据类型，值不可以改变：整型int、浮点型float、字符串型string和元组tuple。


# 【评论区总结一：】：
# 1.可变类型就是一个变量只能对应一个地址，但这个地址可以对应多个值。而不可变类型就是一个变量可以对应多个地址，但每个地址只能对应一个值。
# 2.python中向函数传递参数只能是引用传递，表示把它的地址都传进去了，而非值传递。
#     意思很直观，在调用函数传递参数时，传递的是引用，直白的就是传递对象的内存地址。
#
#     那么，在上面描述的情况中，每次调用主函数返回子函数时，由于return命令的执行，该主函数使用的临时变量的内存都要释放，
#     然而由于返回的子函数使用了主函数的临时变量，这个变量会和子函数绑定，存入该子函数的内存空间。
#
#     当使用L作为这个临时变量或者说传递对象的时候，return子函数这个操作执行后，返回的子函数中的内存空间中存储的L实质上是L指向的内存地址，
#     当进行 **L = L + 1 **这个操作时，由于L现在代表的是一个引用，是一个内存地址，那么实质上的操作就是提取L指向的内存地址中的值；
#     运算该值 + 1的结果；将L指向该结果的内存地址，这个操作需要一个随程序运行更新的起点地址，不然就是一个无法确定运行环境的闭包，而这是与闭包本身的定义相违背的。
#     由于没有设定L为全局变量，所以python就会将这个L视为子函数的局部变量，在子函数内部寻找起点地址，然而又由于未提前在子函数内赋初值，进而报错“局部变量在赋值之前被引用”。

# 【评论区总结二：】：
# 当使用L作为这个临时变量或者说传递对象的时候，return子函数这个操作执行后，在子函数内部，由于并没有声明L是一个全局变量，L所进行的操作也不代表其是一个可变类型的全局变量。
# 接上文，那么L就会被认定为一个局部变量，然而L并没有被赋初值，此时报错“局部变量在赋值之前被引用”。

# 而当L[0]作为一个临时变量或者说传递对象的时候，当执行 L[0] = L[0] + 1这个操作，
# 由于子函数内部在此操作前并没有创建L这个变量，那么触发python认定其为一个可变类型的全局变量，就会往外部寻找，则寻找到之前创建的全局变量L。

# 这个角度的理解方法总结来说，就是python在闭包函数返回子函数时，判定临时变量是否为全局变量的逻辑。
# 当没有声明变量为全局变量时，只有进行了触发python判定其为可变类型的全局变量的操作，才会去外部寻找该变量。那么："触发python判定其为可变类型的全局变量的操作"到底是什么操作呢？
# 所以，当执行 L = L + 1这个操作时，在没有声明L为全局变量的情况下，python是不会去外部寻找的，
# 那么，又因为L并没有在子函数内的开头部分创建，必定会报错“局部变量在赋值之前被引用”。

# 【文章：nonlocal 与 global】https://www.jianshu.com/p/703ad1289a00      ；还有一篇：https://www.cnblogs.com/zhouyang123200/p/6538160.html
# 1.nonlocal意思是告诉python，不要重新创建msg变量，而是使用outside中的msg变量来赋值。
# 2.nonlocal是用来改变变量的作用域的。本例中，nonlocal将inside函数里面的msg变量的作用域变成了outside块中的区域。
# nonlocal跟global 这两个关键字非常像，不同之处在于nonlocal用于外部函数作用域的变量，而global用于全局范围内的变量。

# 【文章：】https://www.cnblogs.com/s-1314-521/p/9763376.html

# 【练习】四种解法的地址：https://www.liaoxuefeng.com/discuss/969955749132672/1339827874168865
def createCounter0():
    c = 0

    def counter():
        nonlocal c  # 这里直接报错：SyntaxError: name 'c' is parameter and nonlocal
        c = c+1
        return c

    return counter

# l是一个可变参数，对l[0]的操作会触发python进行寻找，从而找到是一个全局变量，然后会进行修改。修改以后的值会保留在l指向的地址里面
def createCounter1():
    l = [0]

    def counter():
        l[0] += 1

        return l[0]

    return counter

# 使用了nonlocal关键字，每次不会本地创建一个局部变量，而是修改的是外部函数的变量。从而达到一个记录状态的作用
def createCounter2():
    c = 0

    def counter():
        nonlocal c
        c += 1
        return c

    return counter


if __name__ == "__main__":
    # 测试:
    counterA = createCounter0()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter0()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
