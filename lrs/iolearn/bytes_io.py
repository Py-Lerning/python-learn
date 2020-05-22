from io import BytesIO

if __name__ == '__main__':
    f = BytesIO()
    f.write("你好呀".encode("utf-8"))
    print(f.getvalue())

    f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(f2.read().decode("utf-8"))