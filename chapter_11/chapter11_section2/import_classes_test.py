from chapter_11.chapter11_section2.Point import Point
from chapter_11.chapter11_section2.Rectangle import Rectangle

p = Point(0,0)
q = Point(2,2)
print(p.distance(q))
print(p.reflect_x())

r = Rectangle(Point(0,0),10,5)
print(r.flip())