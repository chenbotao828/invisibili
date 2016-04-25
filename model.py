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


class ClassName(myObject):
    '''docstring for ClassName'''

    def __init__(self, arg):

        typeTest([typeList], arg)
        self.args = (arg)
        self.arg = arg


class Point(myObject):
    '''docstring for Point'''

    def __init__(self, *coords):

        if len(coords) not in [2, 3]:
            raise Exception("Expect 2 or 3 coords, given %d" % len(coords))

        typeTest([Num] * len(coords), *coords)
        self.args = (coords)
        self.x = coords[0]
        self.y = coords[1]
        if len(coords) == 2:
            self.__class__ = type(Point2D(0, 0))
        else:
            self.z = coords[2]
            self.__class__ = type(Point3D(0, 0, 0))


class Point2D(Point):
    '''docstring for Point2D'''

    def __init__(self, x, y):

        typeTest([Num, Num], x, y)
        self.args = (x, y)
        self.x = x
        self.y = y

    def threeD(self, z=0):
        '''docstring for threeD'''

        return Point3D(self.x, self.y, z)


class Point3D(Point):
    '''docstring for Point3D'''

    def __init__(self, x, y, z):

        typeTest([Num, Num, Num], x, y, z)
        self.args = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def twoD(self):
        '''docstring for twoD'''

        return Point2D(self.x, self.y)


class Line(myObject):
    '''2D/3D Line P1 to P2'''

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
        self.center = center
        self.radius = radius


class LWPolyline(myObject):
    '''2D Light weight polyline, composed of Point list'''

    def __init__(self, *points):

        typeTest([Point] * len(points), *points)
        self.args = (points)
        self.points = points


class ellipse(myObject):
    '''docstring for ellipse'''

    def __init__(self, center, major_axis, ratio, start_param=0, end_param=6.283185307):

        typeTest([Point, ], center, major_axis, ratio, start_param, end_param)
        self.args = (center, major_axis, ratio, start_param, end_param)
        self.center = center
        self.major_axis = major_axis
        self.ratio = ratio
        self.start_param = start_param
        self.end_param = end_param


# class Shape(myObject):
#     '''a unity of shapes, including Line, Circle, Arc and
#      LWPolyline'''

#     def __init__(self, *shapes):

#         typeTest([[Line, Circle, Arc, LWPolyline]] * len(shapes), *shapes)
#         self.args = (shapes)
#         self.shapes = shapes

#     def draw(self, modelspace):
#         '''draw a shape in modelspace'''

#         typeTest([Layout], modelspace)
#         pass

# myFunTest(Class().draw, args, goal="goal")
# import ezdxf
# dwg = ezdxf.new('AC1015')
# msp = dwg.modelspace()
