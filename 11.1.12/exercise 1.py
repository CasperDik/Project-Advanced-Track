class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, target):
        dx = self.x - target.x
        dy = self.y - target.y
        result = (dx**2 + dy**2)**0.5
        return result

p = Point(0,0)
q = Point(2,2)
print(p.distance(q))