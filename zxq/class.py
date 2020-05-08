class Point:  # 帕斯卡命名惯例，首字母大写.
    def move(self):
        print("move")

    def draw(self):
        print("draw")


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 100
print(point2.x)


point3 = Point2(11, 22)
print(point3.x, point3.y)


class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def talk(self):
        print(f"Hi, I am {self.name}, I got {self.score}")


john = Person("JohnSmith", 98)                #每个对象都是Person的不同实例
bob = Person("Bob Black", 100)
print(john.name)
print(bob.name)
john.talk()
bob.talk()
