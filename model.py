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

    def __hash__(self):
        return hash((type(self), self.args))


class point(myObject):
    '''docstring for point'''

    def __init__(self, *coords):

        if len(coords) not in [2, 3]:
            raise Exception("Expect 2 or 3 coords, given %d" % len(coords))

        typeTest([Num] * len(coords), *coords)
        self.args = (coords)
        self.x = coords[0]
        self.y = coords[1]
        if len(coords) == 2:
            self.__class__ = type(point2d(0, 0))
        else:
            self.z = coords[2]
            self.__class__ = type(point3d(0, 0, 0))


class point2d(point):
    '''docstring for point2d'''

    def __init__(self, x, y):

        typeTest([Num, Num], x, y)
        self.args = (x, y)
        self.x = x
        self.y = y

    def threeD(self, z=0):
        '''docstring for threeD'''

        return point3d(self.x, self.y, z)


class point3d(point):
    '''docstring for point3d'''

    def __init__(self, x, y, z):

        typeTest([Num, Num, Num], x, y, z)
        self.args = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def twoD(self):
        '''docstring for twoD'''

        return point2d(self.x, self.y)


class vector(myObject):
    '''2D/3D vector'''

    def __init__(self, *coords):

        if len(coords) not in [2, 3]:
            raise Exception("Expect 2 or 3 coords, given %d" % len(coords))

        typeTest([Num] * len(coords), *coords)
        self.args = (coords)
        self.x = coords[0]
        self.y = coords[1]
        if len(coords) == 2:
            self.__class__ = type(vector2d(0, 0))
        else:
            self.z = coords[2]
            self.__class__ = type(vector3d(0, 0, 0))


class vector2d(vector):
    '''docstring for vector2d'''

    def __init__(self, x, y):

        typeTest([Num, Num], x, y)
        self.args = (x, y)
        self.x = x
        self.y = y


class vector3d(vector):
    '''docstring for vector3d'''

    def __init__(self, x, y, z):

        typeTest([Num, Num, Num], x, y, z)
        self.args = (x, y, z)
        self.x = x
        self.y = y
        self.z = z


class line(myObject):
    '''2D/3D line P1 to P2'''

    def __init__(self, p1, p2):

        typeTest([point, point], p1, p2)
        self.args = (p1, p2)
        self.p1 = p1
        self.p2 = p2

    # def offset(self, dis):
    #     '''return Models'''

    #     typeTest([Num], dis)
    #     if isinstance(p1, point2d) and isinstance(p2, point2d):
    #         v = vector(p2.x-p1.x, p2.y-p1.y)
    #     elif:
    #     ret = Models()
    #     ret.db.add()

# myFunTest(Class().offset, args, goal="goal")


class circle(myObject):
    '''2D circle'''

    def __init__(self, center, radius):

        typeTest([point, Num], center, radius)
        self.args = (center, radius)
        self.center = center
        self.radius = radius


class arc(myObject):
    '''docstring for arc'''

    def __init__(self, center, radius, start_angle, end_angle):

        typeTest(
            [point, Num, Num, Num], center, radius, start_angle, end_angle)
        self.args = (center, radius, start_angle, end_angle)
        self.center = center
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle


class lwpolyline(myObject):
    '''2D Light weight polyline, composed of point list'''

    def __init__(self, *points):

        typeTest([point2d] * len(points), *points)
        self.args = (points)
        self.points = points


class ellipse(myObject):
    '''docstring for ellipse'''

    def __init__(self, center, major_axis, ratio, start_param=0, end_param=6.283185307):

        typeTest([point, ], center, major_axis, ratio, start_param, end_param)
        self.args = (center, major_axis, ratio, start_param, end_param)
        self.center = center
        self.major_axis = major_axis
        self.ratio = ratio
        self.start_param = start_param
        self.end_param = end_param


class text(myObject):
    '''docstring for text'''

    def __init__(self, text):

        typeTest([str], text)
        self.args = (text)
        self.text = text


class polyline2d(myObject):
    '''docstring for polyline2d'''

    def __init__(self, *points):

        typeTest([point2d] * len(points), *points)
        self.args = (points)
        self.points = points


class polyline3d(myObject):
    '''docstring for polyline3d'''

    def __init__(self, *points):

        typeTest([point3d] * len(points), *points)
        self.args = (points)
        self.points = points


class mtext(myObject):
    '''docstring for mtext'''

    def __init__(self, text):

        typeTest([str], text)
        self.args = (text)
        self.text = text


class Models(myObject):
    '''Models Set'''

    def __init__(self, s=set()):

        self.db = s
        self.args = (self.db,)

    def add(self, model):
        '''add a model to Models '''

        typeTest([myObject], model)
        self.db.add(model)

    def remove(self, model):
        '''remove a model'''

        typeTest([myObject], model)
        self.db.remove(model)

    def clear(self):
        '''clear Model database'''

        self.db.clear()

    def __contains__(self, model):

        return self.db.__contains__(model)

    def __len__(self):

        return self.db.__len__()

    def __iter__(self):

        return self.db.__iter__()


    methodlist = ["issubset", "__or__","__sub__","__ne__"]
    for i in methodlist:
        a = '''def %s(self, other):
            \"X.%s(Y)\"
            typeTest([Models], other)
            a = self.db.%s(other.db)
            if type(a) ==  bool:
                return a
            return Models(a)''' % (i, i, i)
        exec a in globals(), locals()

    # def __and__(self, other):
    #     typeTest([Models], other)
    #     return Models(self.db.__and__(other.db))

#     def __or__(self, other):
#         "x|y"

#         typeTest([Models], other)
#         return Models(self.db.__or__(other.db))

#     def __sub__(self, other):
#         "x-y"

#         typeTest([Models], other)
#         return Models(self.db.__sub__(other.db))
#     def __ne__(self, other):
#         "x-y"

#         typeTest([Models], other)
#         return Models(self.db.__ne__(other.db))

#     def isdisjoint(self, other):
#         "x-y"

#         typeTest([Models], other)
#         return Models(self.db.isdisjoint(other.db))

#     def issubset(self, other):
#         "x-y"

#         typeTest([Models], other)
#         return Models(self.db.issubset(other.db))
# ----------------------

a = Models({point2d(1, 1), point2d(2, 2)})
b = Models({point2d(1, 1), point2d(2, 2)})
print a.__or__(b)


class Wall(myObject):
    '''Wall object'''

    def __init__(self, base, width=200, hight=3000, align="center"):

        typeTest([Models, Num, Num, str], base, width, hight, align)
        self.args = (base, width, hight, align)
        self.base = base
        self.width = width
        self.hight = hight
        self.align = align

    # def outline(self):
    #     '''return Models'''

    #     ret = Models()
    #     for m in self.base.db:
    #         if m.__class__.__name__ in []


# myFunTest(Class().outline, args, goal="goal")
