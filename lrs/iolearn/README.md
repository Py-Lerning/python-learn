## IO操作介绍
在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的应用程序直接操作磁盘，读写文件就是请求操作系统打开一个文件对象（文件描述符）

通过操作系统提供的接口从这个文件对象中读取数据，或者把数据写入这个文件对象。

## 文件读取
```python
file_path = "test.txt"
f = open(file_path, "r")
f2 = open(file_path, "w")
f3 = open(file_path, "a")
```

## 内存读写
数据读写不一定非要读写文件，也可以在内存中读写。

StringIO在内存中读写str

BytesIO在内存中读写bytes