class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        area = self.height * self.width
        return area

    def perimeter(self):
        perimeter = 2*self.width + 2*self.height
        return perimeter

    def flip(self):
        x = self.width
        y = self.height
        return "({0}, {1}, {2})".format(self.corner, y, x)

    def contains(self, point):
        h = self.corner.y + self.height
        w = self.corner.x + self.width
        if point.x < w and point.x >= self.corner.x:
            if point.y < h and point.x >= self.corner.y:
                return "point falls within the rectangle"
            else:
                return "point does not fall within the rectangle"
        else:
            return "point does not fall within the rectangle"

