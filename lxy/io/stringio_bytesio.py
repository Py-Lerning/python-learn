#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO

abc = 'string \nfrom \noutputstring \nfunction'

def stringio_read():
    # 将函数返回的数据在内存中读
    sio = StringIO(abc)
    # 可以用StringIO本身的方法
    print(sio.getvalue())

    print("----")
    # 也可以用file-like object的方法
    s = sio.readlines()
    for i in s:
        print(i.strip())

def stringio_write():
    # 将函数返回的数据在内存中写
    sio = StringIO()
    sio.write(abc)
    # 可以用StringIO本身的方法查看
    s = sio.getvalue()
    print(s)

    print("-----")
    # 如果你用file-like object的方法查看的时候，你会发现数据为空
    sio = StringIO()
    sio.write(s)
    print(sio.tell())
    for i in sio.readlines():
        print(i.strip())

    print("修改指针位置：")
    # 这时候我们需要修改下文件的指针位置
    # 我们发现可以打印出内容了
    sio = StringIO()
    sio.write(s)

    # sio是一个追加行为
    sio.write("aaaaaaa")
    sio.seek(0, 0)
    print(sio.tell())
    for i in sio.readlines():
        print(i.strip())

    # 这就涉及到了两个方法seek 和 tell
    # tell 方法获取当前文件读取指针的位置
    # seek 方法，用于移动文件读写指针到指定位置,有两个参数，
    # 第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；
    # 第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾

    # 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值哦

def bytes_io():
    # stringIO 只能操作str，如果要操作二进制数据，就需要用到BytesIO
    # 上面的sio无法用seek从当前位置向前移动，这时候，我们用'b'的方式写入数据，就可以向前移动了
    bio = BytesIO()
    bio.write(abc.encode('utf-8'))
    print(bio.getvalue())
    print(bio.tell())   # 36
    bio.seek(-36, 1) # 从当前位置，往前走36个长度
    print(bio.tell()) # 0，走到了0的位置

    for i in bio.readlines():
        print(i.strip())
if __name__ == "__main__":
    # stringio_read()
    # stringio_write()

    bytes_io()