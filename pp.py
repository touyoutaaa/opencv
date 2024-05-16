class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("宽度必须是一个大于0的浮点数或整数")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("高度必须是一个大于0的浮点数或整数")
        self.__height = value
    @property
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    @property
    def side_length(self):
        return self.width

    @side_length.setter
    def side_length(self, value):
        self.width = value
        self.height = value

if __name__ == "__main__":
    square = Square(5)
    print("正方形的边长:", square.side_length)
    print("正方形的面积:", square.area)

