# 类属性和实例属性
class Student(object):
    count = 0

    def __init__(self, name):
        Student.count = Student.count + 1
        self.name = name


if __name__ == "__main__":
    stu1 = Student("stu1")
    stu2 = Student("stu2")
    print(Student.count)