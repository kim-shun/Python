class Point:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def output(self):
        print('Point(%d,%d)'%(self._x, self._y))

p1 = Point(1,2)
p2 = Point(3,4)
p1.output()
p2.output()
