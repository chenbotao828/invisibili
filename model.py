# coding=utf-8
from __future__ import division
from core import _const, myFunTest, myProTest, typeTest


"define const data"
const = _const()

"type of numbers"
Num = const.Num = [int, float, long]

'''
-------------------------------------------------------------------------------
Models of invisibili
-------------------------------------------------------------------------------
'''


class myObject(object):
    "modified Object"

    def __init__(self, *args):
        pass

    def __repr__(self):
        if type(self.args) != tuple:
            return type(self).__name__ + "(" + str(self.args) + ")"
        return type(self).__name__ + str(self.args)

    def __eq__(self, another):
        # sd == ad:
        if type(self) == type(another) and self.args == another.args:
            return True
        return False

class Wall(myObject):
    '''Wall object'''

    def __init__(self, base, width=200, hight=3000, align="center"):

        typeTest([Shape, Num, Num, Str], base, width, hight, align)
        self.args = (base, width, hight, align)
        self.base = base
        self.width = width
        self.hight = hight
        self.align = align


class Point(myObject):
    '''2D Point'''

    def __init__(self, x, y):

        typeTest([Num, Num], x, y)
        self.args = (x, y)
        self.x = x
        self.y = y

class Line(myObject):
    '''2D Line P1 to P2'''

    def __init__(self, p1, p2):

        typeTest([Point, Point], p1, p2)
        self.args = (p1, p2)
        self.p1 = p1
        self.p2 = p2

class Circle(myObject):
    '''2D Circle'''

    def __init__(self, center, radius):

        typeTest([Point, Num], center, radius)
        self.args = (center, radius)
        self.cn = cn

class LWPolyline(myObject):
    '''2D Light weight polyline, composed of Point list'''

    def __init__(self, *Point):

        typeTest([Point]*len(Point), *Point)
        self.args = (Point)
        self.Point = Point
a = LWPolyline(Point(0,0), Point(2,2))
print a 

class Shape(myObject):
    '''an object of shape entities, including Line, Circle, Arc and
     LWPolyline'''

    def __init__(self, ):

        typeTest([typeList], arg)
        self.args = (arg)
        self.arg = arg


myFunTest(Wall, args, goal="goal")

myFunTest(Wall, args, goal="goal")
