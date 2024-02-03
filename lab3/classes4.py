import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

x1 = float(input())
y1 = float(input())
point1 = Point(x1, y1)

x2 = float(input())
y2 = float(input())
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2)
print(distance)

new_x = float(input())
new_y = float(input())
point1.move(new_x, new_y)

point1.show()