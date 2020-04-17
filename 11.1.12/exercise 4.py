class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def linear_equation(self, other):
        a = (other.y - self.y) / (other.x - self.x)
        b = self.y - (a * self.x)
        return "({0}, {1})".format(a, b)

p = Point(1,1)
q = Point(5,5)
print(p.linear_equation(q))

# will fail when point are the same