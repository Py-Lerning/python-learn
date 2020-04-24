import types
# 获取对象信息
class Animal(object):

    def run(self):
        print("Animal is running ......")

    def __test(self):
        print("test")


class Dog(Animal):
    def run(self):
        print("Dog is running ......")


class Cat(Animal):
    def __init__(self):
        self.name = "cat"
        self.age = 1

    def run(self):
        print("Cat is running ......")


if __name__ == "__main__":
    # 基本类型可以直接写int str
    print(type(123))
    print(type(123) == int)
    print(type("123"))
    print(type("123") == str)

    # 判断一个对象是否是函数，可以用types中定制的内容
    def fn():
        pass
    print(type(fn))
    print(type(fn) == types.FunctionType)
    print(type(abs))
    print(type(lambda x:  x + 1))
    print(type(lambda x: x + 1) == types.LambdaType)
    print(type(x for x in range(10)))
    print(type(x for x in range(10)) == types.GeneratorType)

    # 判断某个对象是否是某些类型中的一个，可以用isinstance
    dog = Dog()
    cat = Cat()
    print(isinstance(dog, Animal))
    print(isinstance(cat, Animal))
    print(isinstance(dog, Dog))
    print(isinstance(cat, Cat))
    print(isinstance(cat, Dog))

    # 使用__dir__获取一个对象的所有属性和方法，私有属性和私有方法会变为_Animal__test
    animal = Animal()
    print(dog.__dir__())
    print(animal.__dir__())

    # 判断属性存在与否，
    if hasattr(cat, "name"):
        print(getattr(cat, "name"))
        setattr(cat, "name", "cat-miao")
        print(getattr(cat, "name"))








