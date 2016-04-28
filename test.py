# coding=utf-8
from model import *
from arc import *

# print vector(1,1,1).clockwise(2)
# myFunTest(circle(point(1,1), -32).offset, 2, goal="goal")
# p = point(1, 2, 3)
# q = point(4, 4)

# v = vector(1, 1, 1)
# v2 = vector(1, 1)

# print p.move(v)
# print p.move(v2)
# print q.move(v)
# print q.move(v2)
# a=Models({point(4,2)})
# a.replace(point(4,2), point(1,1))
# print a
# v1 = vector(1, 1)
# v2 = vector(2, 2)

# print v1 * v2

# a=point(2,3,3)

# print a

# b = lwpolyline(point2d(1,1), point2d(2,2), point2d(3,3))

# print b
m = Models({point2d(3,3),point2d(1,1)})
print m
class ClassName(myObject):
    '''docstring for ClassName'''

    def __init__(self, arg):

        typeTest([typeList], arg)
        self.para = tuple("arg".split(", "))
        self.arg = arg
