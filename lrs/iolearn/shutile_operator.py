import shutil
import os

if __name__ == '__main__':
    print([x for x in os.listdir(".") if os.path.isdir(x)])  # 列出虽有的目录
    print([x for x in os.listdir(".")])  # 列出所有的文件+目录
    print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"])  # 列出所有的py文件

    shutil.copyfile("test.txt", "info.txt")
