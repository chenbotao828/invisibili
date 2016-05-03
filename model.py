# coding=utf-8
from __future__ import division
from core import _const, myObject, fun, typeTest, sympy2m
from sympy import *
import math

"define const data"
const = _const()

"type of numbers"
const.N = [int, float, long]
'''
-------------------------------------------------------------------------------
Models of invisibili
-------------------------------------------------------------------------------
'''


class point(myObject):
    '''point'''

    def __init__(self, *coords):

        if len(coords) not in [2, 3]:
            raise Exception("Expect 2 or 3 coords, given %d" % len(coords))

        typeTest([const.N] * len(coords), *coords)
        self.x = coords[0]
        self.y = coords[1]
        if len(coords) == 2:
            self.para = ("x", "y")
            self.__class__ = type(point2d(0, 0))
        else:
            self.para = ("x", "y", "z")
            self.z = coords[2]
            self.__class__ = type(point3d(0, 0, 0))

    def move(self, v):
        '''vector move'''

        typeTest([vector], v)
        if isinstance(self, point2d):
            if isinstance(v, vector2d):
                return point(self.x + v.x, self.y + v.y)
            if isinstance(v, vector3d):
                return point(self.x + v.x, self.y + v.y, v.z)
        elif isinstance(self, point3d):
            if isinstance(v, vector2d):
                return point(self.x + v.x, self.y + v.y, self.z)
            if isinstance(v, vector3d):
                return point(self.x + v.x, self.y + v.y, self.z + v.z)


class point2d(point):
    '''point2d'''

    def __init__(self, x, y):
        point.__init__
        typeTest([const.N, const.N], x, y)
        self.para = ("x", "y")
        self.x = x
        self.y = y

    def threeD(self, z=0):
        '''threeD'''

        return point3d(self.x, self.y, z)


class point3d(point):
    '''point3d'''

    def __init__(self, x, y, z):

        typeTest([const.N, const.N, const.N], x, y, z)
        self.para = ("x", "y", "z")
        self.x = x
        self.y = y
        self.z = z

    def twoD(self):
        '''twoD'''

        return point2d(self.x, self.y)


class vector(myObject):
    '''2D/3D vector, can use 2 points as args, vector from A to B'''

    def __init__(self, *args):

        if len(args) == 2 and isinstance(args[0], point) and\
                args[1].__class__ == args[1].__class__:
            p1 = args[0]
            p2 = args[1]
            args = []
            for i in range(len(p1.args)):
                args.append(p2.args[i] - p1.args[i])
        if len(args) not in [2, 3]:
            raise Exception("Expect 2 or 3 args, given %d" % len(args))

        typeTest([const.N] * len(args), *args)

        self.x = args[0]
        self.y = args[1]
        if len(args) == 2:
            self.para = ("x", "y")
            self.__class__ = type(vector2d(0, 0))
        else:
            self.para = ("x", "y", "z")
            self.z = args[2]
            self.__class__ = type(vector3d(0, 0, 0))

    def __sub__(self, another):

        typeTest([self.__class__], another)
        new = map(lambda x, y: x - y, self.args, another.args)
        return eval(fun(vector, new))

    def __add__(self, another):

        typeTest([self.__class__], another)
        new = map(lambda x, y: x + y, self.args, another.args)
        return eval(fun(vector, new))

    def __mul__(self, another):

        typeTest([const.N + [self.__class__]], another)
        if self.__class__ == another.__class__:
            return sum(map(lambda x, y: x * y, self.args, another.args))
        else:
            new = tuple(x * another for x in self.args)
            return eval(fun(vector, new))

    @property
    def length(self):

        return sum(x**2 for x in self.args)**0.5

    @property
    def unit(self):

        if self.length == 0:
            return self
        a = tuple(x / self.length for x in self.args)
        return eval(fun(vector, a))

    @property
    def slope(self):
        '''slope'''
        if self.x == 0:
            if self.y > 0:
                return float('inf')
            return -float('inf')
        return self.y / self.x

    def clw(self, n=1):
        '''clockwise 90 degrees for n times, counter-clockwise if n<0'''

        typeTest([int], n)
        ret = self
        for i in range(n % 4):
            if isinstance(ret, vector2d):
                ret = vector(ret.y, -ret.x)
            else:
                ret = vector(ret.y, -ret.x, ret.z)
        return ret

    def rotate2d(self, rad=math.pi / 2, clw=True):
        '''rotate vector, measured in radians, clw 90 deg. by default,
        (loss of significance)'''

        typeTest([bool], clw)
        if not clw:
            rad = -rad
        y = math.tan(rad - math.atan(self.y / self.x))
        ret = vector(1, y).unit * self.length
        return ret


class vector2d(vector):
    '''vector2d'''

    def __init__(self, x, y):

        typeTest([const.N, const.N], x, y)
        self.para = ("x", "y")
        self.x = x
        self.y = y


class vector3d(vector):
    '''vector3d'''

    def __init__(self, x, y, z):

        typeTest([const.N, const.N, const.N], x, y, z)
        self.para = ("x", "y", "z")
        self.x = x
        self.y = y
        self.z = z


class line(myObject):
    '''2D/3D line P1 to P2'''

    def __init__(self, p1, p2):

        typeTest([point, p1.__class__], p1, p2)
        self.para = ("p1", "p2")
        self.p1 = p1
        self.p2 = p2

    def offset(self, dis):
        '''return a parallel of a line, the direction vector is
        clw compare with the vector(p1, p2) if dis > 0'''

        typeTest([const.N], dis)

        v = vector(self.p2.x - self.p1.x,
                   self.p2.y - self.p1.y).clw().unit * dis
        return self.move(v)

    def angle_between(self, another):
        '''Angle between two lines, measured in radians'''

        typeTest([line], another)
        p1 = eval(fun(Point, self.p1.args))
        p2 = eval(fun(Point, self.p2.args))
        p3 = eval(fun(Point, another.p1.args))
        p4 = eval(fun(Point, another.p2.args))
        l1, l2 = Line(p1, p2), Line(p3, p4)
        return float(l1.angle_between(l2))

    @property
    def sympy(self):
        '''return sympy Segment'''

        return eval("Segment" + self.args.__repr__().title())

    @property
    def Line(self):
        '''return sympy Line'''

        return eval("Line" + self.args.__repr__().title())

    @property
    def length(self):
        '''return length'''

        return vector(self.p1, self.p2).length

    @property
    def slope(self):
        '''slope'''

        return vector(self.p1, self.p2).slope

    def merge(self, another):
        '''merge two colinear lines'''

        typeTest([line], another)
        il = self.sympy.intersection(another.sympy)
        if il != [] and isinstance(il[0], Segment):
            p1, p2 = self.p1, self.p2
            p3, p4 = another.p1, another.p2
            pl = [p1, p2, p3, p4]
            if self.slope in [float("inf"), -float("inf")]:
                pl.sort(lambda a, b: cmp(a.y, b.y))
            else:
                pl.sort(lambda a, b: cmp(a.x, b.x))
            return line(pl[0], pl[-1])
        raise ValueError("Expect overlapped lines")


class circle(myObject):
    '''2D circle'''

    def __init__(self, center, radius):

        typeTest([point, const.N], center, radius)
        self.para = ("center", "radius")
        self.center = center
        self.radius = abs(radius)

    def offset(self, dis):
        '''outwards if dis > 0'''

        typeTest([const.N], dis)
        assert self.radius + dis >= 0
        return circle(self.center, self.radius + dis)


class arc(myObject):
    '''arc'''

    def __init__(self, center, radius, start_angle, end_angle):

        typeTest([point, const.N, const.N, const.N],
                 center, radius, start_angle, end_angle)
        self.para = ("center", "radius", "start_angle", "end_angle")
        self.center = center
        self.radius = abs(radius)
        self.start_angle = start_angle
        self.end_angle = end_angle

    def offset(self, dis):
        '''outwards if dis > 0'''

        typeTest([const.N], dis)
        assert self.radius + dis >= 0
        return arc(self.center, self.radius + dis,
                   self.start_angle, self.end_angle)


class lwpolyline(myObject):
    '''2D Light weight polyline, composed of point list'''

    def __init__(self, *points):

        typeTest([point2d] * len(points), *points)
        self.para = ("*points",)
        self.points = points
        assert len(self.args) >= 2


def Function(Parameters):
    '''docstring for Function'''

    typeTest([typeList], Parameters)
    pass
    # def offset(self, dis):
    #     '''Offset lwpolyline like line'''

    #     def new_p(p, dis, pre_p, post_p):
    #         if vector(pre_p, p).slope == vector(p, post_p).slope:
    #             return p.move(vector(pre_p, p).clw().unit * dis)
    #         else:
    #             pre_l = line(pre_p, p).offset(dis)
    #             post_l = line(p, post_p).offset(dis)
    #             if post_l.length == 0:
    #                 ret = p.move(vector(pre_p, p).clw().unit * dis)
    #             if pre_l.length == 0:
    #                 ret = p.move(vector(p, post_p).clw().unit * dis)
    #             else:
    #                 ret = eval(sympy2m(pre_l.Line.intersection(post_l.Line)[0]))
    #             return ret

    #     new_start = self.args[0].move(
    #         vector(self.args[0], self.args[1]).clw().unit * dis)
    #     new_end = self.args[-1].move(
    #         vector(self.args[-2], self.args[-1]).clw().unit * dis)
    #     new_arg = [new_start]
    #     new_arg += map(lambda i: new_p(self.args[i], dis, self.args[i - 1],
    #                                    self.args[i + 1]),
    #                    range(1, len(self.args) - 1))
    #     new_arg += [new_end]

    #     return eval(fun(lwpolyline, new_arg))

    @property
    def sympy(self):
        '''return sympy segments lists'''

        ret = []
        points = self.points
        for i in range(1, len(points)):
            ret.append(Segment(points[i - 1].sympy, points[i].sympy))
        return ret

    def intersection(self, another):
        '''only for lines and lwpolylines'''

        typeTest([[line, lwpolyline]], another)
        ret = []
        if isinstance(another, lwpolyline):
            for i in self.sympy:
                for j in another.sympy:
                    ret += i.intersection(j)
        if isinstance(another, line):
            for i in self.sympy:
                ret += i.intersection(another.sympy)
        return Models(map(lambda x: eval(sympy2m(x)), list(set(ret))))


class ellipse(myObject):
    '''ellipse'''

    def __init__(self, center, major_axis, ratio, start_param=0,
                 end_param=math.pi * 2):

        typeTest([point, const.N, const.N, const.N], center,
                 major_axis, ratio, start_param, end_param)
        self.para = ("center", "major_axis", "ratio",
                     "start_param", "end_param")
        self.center = center
        self.major_axis = abs(major_axis)
        self.ratio = abs(ratio)
        self.start_param = start_param
        self.end_param = end_param


class text(myObject):
    '''text'''

    def __init__(self, text):

        typeTest([str], text)
        self.para = ("text",)
        self.text = text


class polyline2d(myObject):
    '''polyline2d'''

    def __init__(self, *points):

        typeTest([point2d] * len(points), *points)
        self.para = ("*points",)
        self.points = points


class polyline3d(myObject):
    '''polyline3d'''

    def __init__(self, *points):

        typeTest([point3d] * len(points), *points)
        self.para = ("*points",)
        self.points = points


class mtext(myObject):
    '''mtext'''

    def __init__(self, text):

        typeTest([str], text)
        self.para = ("text",)
        self.text = text


class Models(set):
    '''model set'''

    def replace(self, old, new):
        "replace old to new one"

        typeTest([myObject, myObject], old, new)
        self.remove(old)
        self.add(new)

    def move(self, v):
        '''move model position'''

        typeTest([vector], v)
        ret = Models()
        for m in self:
            ret.add(m.move(v))
        return ret
