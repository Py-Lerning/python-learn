import os

if __name__ == '__main__':
    print(os.uname())  # 操作系统类型,和详细信息
    print(os.environ)  # 环境变量
    print(os.environ.get("PATH"))  # 获取某种环境变量
    print(os.path.abspath("."))  # 当前的绝对路径
    print(os.path.join(os.path.abspath("."), "testdir"))  # 不要用字符串拼接，要用join以争取处理不同操作系统的路径分割符
    if os.path.exists(os.path.join(os.path.abspath("."), "testdir")):
        os.rmdir(os.path.join(os.path.abspath("."), "testdir"))
    os.mkdir(os.path.join(os.path.abspath("."), "testdir"))

    path_name = os.path.abspath(".")

    print(os.path.split(path_name))
    print(os.path.splitext("test.txt"))

    os.rename('testdir', "newdir")
