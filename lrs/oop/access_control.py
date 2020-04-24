class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender


# 访问控制，将name 和 gender 属性隐藏起来
if __name__ == '__main__':
    stu = Student("a", "male")
    print("Student name: " + str(stu.get_name()))
    print("Student gender: " + str(stu.get_gender()))



