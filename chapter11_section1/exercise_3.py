class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        slope = self.y / self. x
        return slope

p = Point(5,10)
print(p.slope_from_origin())