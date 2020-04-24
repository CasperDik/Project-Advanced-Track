class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distance(self, target):
        dx = self.x - target.x
        dy = self.y - target.y
        result = (dx**2 + dy**2)**0.5
        return result

    def reflect_x(self):
        reflect = -(self.y)
        return "({0}, {1})".format(self.x, reflect)

    def slope_from_origin(self):
        slope = self.y / self. x
        return slope

    def linear_equation(self, other):
        a = (other.y - self.y) / (other.x - self.x)
        b = self.y - (a * self.x)
        return "({0}, {1})".format(a, b)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):               #e.g. (3,3)*(3,3)= (9,9)
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):                  #e.g. 4 * (3,3) = (12,12)
        return Point(other * self.x, other * self.y)