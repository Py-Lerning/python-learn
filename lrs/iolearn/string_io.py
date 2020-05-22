from io import StringIO


if __name__ == '__main__':
    f = StringIO()
    f.write("Hello ")
    f.write("World ")
    print(f.read())  # is null, why?
    print(f.getvalue())
    print(f.readline()) # is null, why?
    f.flush()
    print(f.readline()) # in null, why?

    f2 = StringIO("Hello World\n你好呀！")
    print(f2.getvalue())