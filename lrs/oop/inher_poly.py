# 继承和多态
class Animal(object):

    def run(self):
        print("Animal is running ......")

    def __test(self):
        print("test")


class Dog(Animal):
    def run(self):
        print("Dog is running ......")


class Cat(Animal):
    def run(self):
        print("Cat is running ......")


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == "__main__":
    run_twice(Dog())
    run_twice(Cat())
    print(type(Dog()))
    print(type(Cat()))

# 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# 动态语言可以把父类的所有功能都直接拿过来，不必从零开始。不包括各种私有功能


