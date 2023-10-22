'''
You are given four points `A`, `B`, `C` and `D` in a 3-dimensional 
Cartesian coordinate system. You are required to print the angle between 
the plane made by the points `A,B,C` and `B,C,D` in degrees(not radians). 
Let the angle be `PHI`.

`Cos(PHI) = (X.Y)/|X||Y| where X=ABxBC  and Y=BCxCD.

Here, `X.Y` means the dot product of `X` and `Y`, and `ABxBC`  means the 
cross product of vectors `AB` and `BC`. Also, AB=B-A.
'''

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, no):
        X = self.x - no.x
        Y = self.y - no.y
        Z = self.z - no.z
        return Points(*[X,Y,Z])

    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        X = self.y*no.z - no.y*self.z
        Y = -self.x*no.z + no.x*self.z
        Z = self.x*no.y - no.x*self.y
        return Points(*[X,Y,Z])
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))