#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 【文章：】https://www.runoob.com/python/python-object.html

# Python内置类属性
# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

# 【文章：】https://blog.csdn.net/qq_38358499/article/details/92774242
# 【总结：】
# 注意1：当在类中定义了构造函数，并且给构造函数设置了参数，系统将不再提供无参的构造函数
# 在创建对象的时候，注意参数的匹配问题
# 注意2：在同一个类中，构造函数只能出现一次
class Student(object):
    # 类变量：
    totalCount = 1

    # 构造函数，而且变量不用声明上去。直接self.xxx使用就行了。self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
    def __init__(self, name, score):
        # < __main__.Student instance at 0x10d066878 >
        print(self)

        # __main__.Student
        print(self.__class__)

        self.name = name
        self.score = score

        # 私有变量
        self.__name = name

    # 析构函数__del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

    # 本来是想搞多个构造函数
    def __init__(self):
        self.name = "harry"
        self.score = 85
        self.count = 1

    def print(self):
        print("%s : %s" % (self.name, self.score))
        if self.count > 0:
            print("有count")
        else:
            print("没有count : %s" % self.count)

        # 如果没有声明过直接就使用，那就直接报错了: 'Student' object has no attribute 'gender'
        print(self.gender)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == "__main__":
    s = Student()
    # s.print()
    print(s.get_grade())

    # 如果我在外面这样执行了一下，然后再调用print，其实是可以在 方法内部用 self.gender 去进行访问的
    s.gender = "male"
    s.print()

    # 下面这一行会报错：TypeError: __init__() takes 1 positional argument but 3 were given
    # s1 = Student("kk", 90)
    # s.print()
    # print(s.get_grade())
