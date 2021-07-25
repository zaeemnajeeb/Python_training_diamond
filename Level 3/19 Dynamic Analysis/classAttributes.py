"""
This is an typical class
"""

class Point:
    'This is a simple 2D point class'
    # define class attribute
    count = 0

    @staticmethod
    def getCount():
        '''define class (static) method'''
        return Point.count

    # CTOR
    def __init__(self, name, x0 = 0, y0 = 0):
        Point.count += 1
        self.name = name
        self.x = x0
        self.y = y0

    def moveBy(self, dx, dy):
        '''how to move a point'''
        self.x += dx
        self.y += dy

    def display(self):
        '''display name and position of point'''
        print("Point {} is at ({},{})".format(self.name, self.x, self.y))

print("No of objects:", Point.getCount())
# create objects
q = Point('origin')
p1 = Point('point-1', 100, 200)
p2 = Point('point-2', 200, 300)
p3 = Point('point-3', 300, 500)
print("No of objects:", Point.getCount())

p1.moveBy(1, 1)
p2.moveBy(2, 3)
p3.moveBy(3, 6)

p1.display()
p2.display()
p3.display()
