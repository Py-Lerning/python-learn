#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any


class ListMetaclass(type):
    # __new__() 方法接收到的参数依次是：
    # 1.  当前准备创建的类的对象；
    # 2.  类的名字；
    # 3.  类继承的父类集合；
    # 4.  类的方法集合。其实还有类属性
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print("\nFound Model:%s" % name)
        mappings = dict()

        # 找所有的类属性。（包括类属性和类方法），如果是继承自Field类型，那就放到mappings中
        for k, v in attrs.items():
            # 打印出来的是：Found mapping: id == > < IntegerField:id >
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 把attrs中的类属性排除
        for k in mappings.keys():
            attrs.pop(k)

        # 说实话不清楚的是，这里attrs算是类属性还是实例属性？应该是类的属性。
        # 执行了 u = User()和car = Car()以后，User和Car类中，对于字段__mappings__和__table__，都已经保存了。
        # 所以User和Car的子类，都可以进行访问了。反正这个和状态无关
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# Model是一个继承自dict的东西
# class Model(object, metaclass=ModelMetaclass):
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        # 这时：self已经有了属性了：{'id': 12345, 'name': 'Michael', 'email': 'test@orm.org', 'password': 'my-pwd'}，
        # 所以是调用了父类的方法
        print()

    # 调用 getattr(self, k, None) 方法时，实际上是调用了这个方法。这个方法进行了重写，从self这个{} 中获取字段。
    # print(u.k)：调用这一句的时候，会调用一下 __getattr__ 方法
    # print(u["k"])：啥都么有
    def __getattr__(self, key):
        print("get了一下变量。%s" % key)
        try:
            # 当成一个字典在用了
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    # 设置变量的时候，就要set到self到这个dict中
    # u["kkk"] = "kkk" ：啥都么有
    # u.k = "kkk" ：调用这一句的时候，会调用一下 __setattr__ 方法
    def __setattr__(self, key, value):
        print("set了一下变量。%s - %s" % (key, value))
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        # 在metaclass中已经set到每个class的__mappings__中了，所以可以直接拿来使用
        for k, v in self.__mappings__.items():
            # 比如说k是id，v是IntegerField
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

            # 当我把Model类中的 __getattr__ 和 __setattr__ 注释掉以后：
            # 其实对于每个对象，他们都是一个dict。然后他们的属性字段值，都可以通过 self[k] 或者 self[v.name]获取到。
            # 但是就无法调用 getattr(self, k, None) 获取到。调用：getattr 方法，就是调用类对象中的：__getattr__ 方法。
            # 但是会报错：{AttributeError}'User' object has no attribute 'id'

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


class Car(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    carname = StringField('carname')


class Test(object):
    count = 1

    def print(self):
        print("这是：", self.count)


class MyList(list, metaclass=ListMetaclass):
    count = 1

    def print(self):
        print("abc")

    pass


if __name__ == "__main__":
    list = MyList()

    # 创建一个实例：
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u1 = User(id=15, name='Michael1', email='test@orm.org1', password='my-pwd1')

    # 保存到数据库：
    u.save()

    car = Car(id=12345, carname='奔驰')
    car.save()

    test = Test()
    test.print()

    # 啥都么有
    u["k1"] = "kkk1"
    print("---", u.__dict__) # --- {}，都是空的。说明u["k1"] = "kkk1"，是把u当成字典用了，根本没放入到类本身的 __dict__ 属性里面

    # 调用这一句的时候，会调用一下 __setattr__ 方法，【但是__setattr__ 魔改过了】
    u.k2 = "kkk2"
    print("---", u.__dict__) # --- {}说明u.k2 = "kkk2"，确实是python中普通object的通用方法，但是__setattr__也魔改过了，也是把u当成字典用了，根本没放入到类本身的 __dict__ 属性里面

    # 调用这一句的时候，会调用一下 __getattr__ 方法
    print(u.k1)

    # 啥都么有。为什么这句就不调用 __getattr__ 了呢？这不也是字典用法吗？
    print(u['k2'])

    # 这句报错：TypeError: 'Test' object does not support item assignment
    # test["test"] = "test"

    # 这句没报错
    test.test = "test"
    print(test.test)

    print(test.__dict__)
