class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        reflect = -(self.y)
        return "({0}, {1})".format(self.x, reflect)

p = Point(4,5)
print(p.reflect_x())