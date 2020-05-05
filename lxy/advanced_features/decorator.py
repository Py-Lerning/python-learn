#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
# 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
import time, functools


def log(func):
    # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
    # 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
    def wrapper1(*args, **kw):
        print("call %s" % func.__name__)
        return func(*args, **kw)

    return wrapper1


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


def log3(func):
    # 类似于做了一个：wrapper.__name__ = func.__name__
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# @log
# now = log(now)
# def now():
#     print('2015-3-25')

# 这个log2("execute")调用以后返回的是decorator这个函数。和上面log函数是一样的
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# now = log('execute')(now)
# 【剖析：】首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
@log2('execute')
def now():
    print('2015-3-25')


# 【课堂练习】
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        # time.time()可以获取当前时间。就像java 里面 System.currentMillseconds
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print('%s executed in %s ms' % (func.__name__, t2 - t1))
        return result

    return wrapper


# 【课后作业】摘抄大神的答案。让这个metric既支持@log('execute')，也支持@log 这样调用
def metric_update(parm):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*arg, **kwarg):
            b = time.time()
            res = fn(*arg, **kwarg)
            e = time.time()
            print('[%s]: %s executed in %s ms' % (parm, wrapper.__name__, e - b))
            # 使用functools.wraps装饰器的作用，就在于获取函数名__name__的时候，可以使用wrapper函数。
            return res

        return wrapper

    # 如果参数是str类型，相当于 @log。那就直接按照原有的方式，返回decorator。然后等外边执行
    if isinstance(parm, str):
        """
        @metric('INFO-FAST')
        def fast(x, y):
            pass
        当使用这种方式时，传入的参数str类型，这个装饰器相当于执行 fast = metric('fast')(fast)
        """
        return decorator

    # 如果参数是函数，相当于 @log。那就相当于手动帮忙执行一下 decorator(parm) 这个函数，拿到一个 wrapper 的函数
    elif callable(parm):  # 使用callable判断参数parm是否为函数
        """
        @metric
        def slow(x, y, z):
            pass
        当使用这种方式时，传入的参数function类型，这个装饰器相当于执行 slow = metric(slow)
        """
        return decorator(parm)


if __name__ == "__main__":
    # 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
    f = now
    print("通过变量直接调用函数：f() ", f())
    # 函数对象有一个__name__属性，可以拿到函数的名字：下面这两个一样的
    print(now.__name__)
    print(f.__name__)

    print("调用函数：now() ", now())
