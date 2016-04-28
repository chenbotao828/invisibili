# coding=utf-8
from __future__ import division
from core import _const, myFunTest, myProTest, typeTest


"define const data"
c = _const()

"type of numbers"
c.N = [int, float, long]
'''
-------------------------------------------------------------------------------
Models of invisibili
-------------------------------------------------------------------------------
'''


class myObject(object):
    "My Object "

    def __init__(self):
        pass

    def __eq__(self, another):
        # sd == ad:
        if type(self) == type(another) and self.__dict__ == another.__dict__:
            return True
        return False

    def __hash__(self):
        return hash((type(self), self.args))

    @property
    def args(self):
        '''args for model'''

        ret = []
        for p in self.para:
            if p[0:2] == "**":
                raise Exception("\"**\" parameter is not allowed")
            if p[0] == "*":
                ret += self.__dict__[p.lstrip("*")]
            else:
                ret.append(self.__dict__[p])
        return tuple(ret)

    def __repr__(self):
        if type(self.args) != tuple:
            return type(self).__name__ + "(" + str(self.args) + ")"
        return type(self).__name__ + str(self.args)


class point(myObject):
    '''docstring for point'''

    def __init__(self, *coords):

        if len(coords) not in [2, 3]:
            raise Exception("Expect 2 or 3 coords, given %d" % len(coords))

        typeTest([c.N] * len(coords), *coords)
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
    '''docstring for point2d'''

    def __init__(self, x, y):

        typeTest([c.N, c.N], x, y)
        self.para = ("x", "y")
        self.x = x
        self.y = y

    def threeD(self, z=0):
        '''docstring for threeD'''

        return point3d(self.x, self.y, z)


class point3d(point):
    '''docstring for point3d'''

    def __init__(self, x, y, z):

        typeTest([c.N, c.N, c.N], x, y, z)
        self.para = ("x", "y", "z")
        self.x = x
        self.y = y
        self.z = z

    def twoD(self):
        '''docstring for twoD'''

        return point2d(self.x, self.y)


class vector(myObject):
    '''2D/3D vector'''

    def __init__(self, *args):

        if len(args) not in [2, 3]:
            raise Exception("Expect 2 or 3 coords, given %d" % len(args))

        typeTest([c.N] * len(args), *args)
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

        if self.__class__ != another.__class__:
            raise TypeError("Expect 2 vector2d/vector3d")
        new = tuple(map(lambda x, y: x - y, self.args, another.args))
        return eval("vector" + str(new))

    def __add__(self, another):

        if self.__class__ != another.__class__:
            raise TypeError("Expect 2 vector2d/vector3d")
        new = tuple(map(lambda x, y: x + y, self.args, another.args))
        return eval("vector" + str(new))

    def __mul__(self, another):

        if self.__class__ != another.__class__:
            raise TypeError("Expect 2 vector2d/vector3d")
        new = sum(map(lambda x, y: x * y, self.args, another.args))
        return new

    @property
    def length(self):

        return sum(x**2 for x in self.args)**0.5

    @property
    def unit(self):

        if self.length == 0:
            return self
        a = tuple(x / self.length for x in self.args)
        return eval("vector" + str(a))

    def clockwise(self, n=1):
        '''clockwise 90 degree for n times'''

        typeTest([int], n)
        ret = self
        for i in range(n):
            if isinstance(ret, vector2d):
                ret = vector(ret.y, -ret.x)
            else:
                ret = vector(ret.y, -ret.x, ret.z)
        return ret


class vector2d(vector):
    '''docstring for vector2d'''

    def __init__(self, x, y):

        typeTest([c.N, c.N], x, y)
        self.para = ("x", "y")
        self.x = x
        self.y = y


class vector3d(vector):
    '''docstring for vector3d'''

    def __init__(self, x, y, z):

        typeTest([c.N, c.N, c.N], x, y, z)
        self.para = ("x", "y", "z")
        self.x = x
        self.y = y
        self.z = z


class line(myObject):
    '''2D/3D line P1 to P2'''

    def __init__(self, p1, p2):

        typeTest([point, point], p1, p2)
        self.para = ("p1", "p2")
        self.p1 = p1
        self.p2 = p2


class circle(myObject):
    '''2D circle'''

    def __init__(self, center, radius):

        typeTest([point, c.N], center, radius)
        self.para = ("center", "radius")
        self.center = center
        self.radius = abs(radius)

    def offset(self, dis):
        '''outwards if dis > 0'''

        typeTest([c.N], dis)
        return circle(self.center, self.radius + dis)


class arc(myObject):
    '''docstring for arc'''

    def __init__(self, center, radius, start_angle, end_angle):

        typeTest([point, c.N, c.N, c.N],
                 center, radius, start_angle, end_angle)
        self.para = ("center", "radius", "start_angle", "end_angle")
        self.center = center
        self.radius = abs(radius)
        self.start_angle = start_angle
        self.end_angle = end_angle


class lwpolyline(myObject):
    '''2D Light weight polyline, composed of point list'''

    def __init__(self, *points):

        typeTest([point2d] * len(points), *points)
        self.para = ("*points",)
        self.points = points


class ellipse(myObject):
    '''docstring for ellipse'''

    def __init__(self, center, major_axis, ratio, start_param=0,
                 end_param=6.283185307):

        typeTest([point, c.N, c.N, c.N], center,
                 major_axis, ratio, start_param, end_param)
        self.para = ("center", "major_axis", "ratio",
                     "start_param", "end_param")
        self.center = center
        self.major_axis = abs(major_axis)
        self.ratio = abs(ratio)
        self.start_param = start_param
        self.end_param = end_param


class text(myObject):
    '''docstring for text'''

    def __init__(self, text):

        typeTest([str], text)
        self.para = ("text",)
        self.text = text


class polyline2d(myObject):
    '''docstring for polyline2d'''

    def __init__(self, *points):

        typeTest([point2d] * len(points), *points)
        self.para = ("*points",)
        self.points = points


class polyline3d(myObject):
    '''docstring for polyline3d'''

    def __init__(self, *points):

        typeTest([point3d] * len(points), *points)
        self.para = ("*points",)
        self.points = points


class mtext(myObject):
    '''docstring for mtext'''

    def __init__(self, text):

        typeTest([str], text)
        self.para = ("text",)
        self.text = text


class Models(myObject):
    '''model collection like set'''

    def __init__(self, db=set()):

        self.db = db
        self.para = ("db",)

    def add(self, *model):
        '''add one or more model'''

        typeTest([myObject] * len(model), *model)
        # if not isinstance(model, tuple):
        if len(model) == 1:
            self.db.add(model)
        else:
            for m in model:
                self.db.add(m)

    def copy(self):
        '''return a shallow copy of a set'''

        return Models(self.db.copy())

    def remove(self, model):
        '''remove a model'''

        typeTest([myObject], model)
        self.db.remove(model)

    def discard(self, model):
        '''remove a model, do nothing if not exist'''

        typeTest([myObject], model)
        self.db.discard(model)

    def clear(self):
        '''clear Model database'''

        self.db.clear()

    def __contains__(self, model):

        return self.db.__contains__(model)

    def __len__(self):

        return self.db.__len__()

    def __iter__(self):

        return self.db.__iter__()

    def pop(self):

        return self.db.pop()

    def replace(self, old, new):

        self.remove(old)
        self.add(new)

    setMethods = ["__and__", "__ge__", "__gt__", "__iand__",
                  "__ior__", "__isub__", "__ixor__", "__le__", "__lt__",
                  "__ne__", "__or__", "__rand__", "__ror__", "__rsub__",
                  "__rxor__", "__sub__", "__xor__", "difference",
                  "difference_update", "intersection", "intersection_update",
                  "isdisjoint", "issubset", "issuperset",
                  "symmetric_difference", "symmetric_difference_update",
                  "union", "update"]
    for method in setMethods:
        a = '''def %s(self, other):
            typeTest([Models], other)
            a = self.db.%s(other.db)
            if not isinstance(a, Models):
                return a
            return Models(a)''' % (method, method)
        exec a in globals(), locals()


# def replaceArg(model, oldArg, newArg):
#     '''docstring for replaceArg'''

#     typeTest([myObject, int], model, argIndex)
#     m = model.__class__.name
#     args = model.args
#     return eval(m + "(" + args + ")")

# myFunTest(replaceArg, args, goal="goal")


# def move(v, models):
#     '''move model position using vector'''

#     typeTest([vector, myObject], v, model)
#     if not isinstance(model, Models):
#         newargs = model.args[:]
#         for arg in model.args:
#             if isinstance(arg, point):
#                 new
