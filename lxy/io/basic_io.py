#!/usr/bin/env python3
# -*- coding: utf-8 -*-

jpg_path = '/Users/harryliu/py_code/python-learn/lxy/io/kanshan.jpg'
file_path = '/Users/harryliu/py_code/python-learn/lxy/io/abc'

def basic_read_str():
    # 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
    f = open(file_path, 'r')

    # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
    print(f.read())
    # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
    f.close()

    # 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
    # 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
    try:
        f = open(file_path, 'r')
        print(f.read())
    except IOError as e:
        print(e)
    finally:
        if f:
            f.close()

    # Python引入了with语句来自动帮我们调用close()方法：
    with open(file_path, 'r') as f:
        print(f.read())

    # 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)
    # 方法，每次最多读取size个字节的内容。
    #
    # 另外，调用readline()可以每次读取一行内容
    # 调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
    #
    # 1.  如果文件很小，read() 一次性读取最方便；
    # 2.  如果不能确定文件大小，反复调用read(size)比较保险；
    # 3.  如果是配置文件，调用readlines()最方便：

    with open(file_path, 'r') as f:
        for line in f.readlines():
            print(line)
            print(line.strip())  # 把末尾的'\n'删掉

# 二进制文件
def basic_read_binary():
    f = open(jpg_path, 'rb')
    print(f.read())
    f.close()

# 字符编码
def read_with_encode():
    f = open(file_path, 'r', encoding='gbk')
    print(f.read())
    f.close()


# 写文件
def basic_write():
    # 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入
    # 'a'以追加（append）模式写入。
    f = open(file_path, 'w',encoding="utf8")
    f.write("新写入的1")
    f.close()


    f = open(file_path, 'a',encoding="utf8")
    f.write("新写入的2")
    f.close()
# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
#
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
if __name__ == "__main__":
    # basic_read_binary()
    #
    # read_with_encode()

    basic_write()