if __name__ == '__main__':
    f_path = "test.txt"

    with open(f_path, "r") as f:
        s1 = f.readline()
        print(s1)
        s = f.read()
        print(s)

    with open(f_path, "a") as f:
        f.write("我也喜欢Python呀!\n")
        f.write("Me too!\n")

    with open(f_path, "r") as f:
        s = f.read()
        print(s)

    with open(f_path, "r") as f:
        for line in f.readlines():
            print(line.strip())