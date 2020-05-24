#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct


# [Python3 bytes 函数](https://www.runoob.com/python3/python3-func-bytes.html)

# 语法
# 以下是 bytes 的语法:
#
# class bytes([source[, encoding[, errors]]])
# 参数
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。


# [python--数据类型bytes](https://www.cnblogs.com/R-bear/p/7744454.html)
# [Python bytes类型及用法](http://c.biancheng.net/view/2175.html)


# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
#
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

# struct模块定义的数据类型可以参考Python官方文档：
#
# https://docs.python.org/3/library/struct.html#format-characters
def read_windows_bmp():
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    unpack = struct.unpack('<ccIIIIIIHH', s)

    # 结果：(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
    print(unpack)

# 交作业
def bmp_info(data):
    try:
        x = struct.unpack('<ccIIIIIIHH', data[0:30])
        return {
            'width': x[6],

            'height': x[7],

            'color': x[9]
        }
    except:
        return None


if __name__ == "__main__":
    n = 10240099
    b1 = (n & 0xff000000) >> 24
    b2 = (n & 0xff0000) >> 16
    b3 = (n & 0xff00) >> 8
    b4 = n & 0xff
    bs = bytes([b1, b2, b3, b4])
    print(bs)  # b'\x00\x9c@c'
    bs2 = '10240099'.encode()
    print(bs2)  # b'10240099'

    # pack的第一个参数是处理指令，'>I'的意思是：
    #
    # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    #
    # 后面的参数个数要和处理指令一致。
    print(struct.pack('>I', 10240099))

    # 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
    # 结果：(10240099,)
    print(struct.unpack('>I', b'\x00\x9c@c'))

    # 结果：(4042322160, 32896)
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

    read_windows_bmp();
