# 使用property，装饰setter getter
class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__height * self.__width


if __name__ == "__main__":
    screen = Screen()
    screen.height = 12
    screen.width = 13
    # screen.resolution = 1231 # read only
    print(screen.width)
    print(screen.height)
    print(screen.resolution)