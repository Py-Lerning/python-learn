# 使用slot限制属性
class Student(object):
    __slots__ = ('name', 'age')

    def __str__(self):
        return str(self.name) + " " + str(self.age)


class GoodStudent(Student):
    __slots__ = 'grade'

    def __str__(self):
        return str(self.name) + " " + str(self.age) + " " + str(self.grade)


if __name__ == "__main__":
    s = Student()
    s.name = "name"
    s.age = 12
    print(s)
    # 子类的slot为子类加父类slot的和
    gs = GoodStudent()
    gs.name = "name"
    gs.age = 12
    gs.grade = "Q"
    print(gs)
