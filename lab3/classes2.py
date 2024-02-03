class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print(shape.area())

length = float(input())
square = Square(length)
print(square.area())