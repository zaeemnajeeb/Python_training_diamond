############################################################
#
#       Type hints: classes
#
############################################################

class Point:
    count: int = 0

    def __init__(self, x0:int, y0:int)->None:
        Point.count += 1
        self.x = x0
        self.y = y0

    @staticmethod        # required by mypy
    def getCount()->int:
        return Point.count


p1 = Point(5, 9)
p2 = Point(4, 8)
p3 = Point(3, 7)

print(Point.getCount())

#):
############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
