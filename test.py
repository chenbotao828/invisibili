# coding=utf-8
from __future__ import division
from model import *
from arc import *
from core import *


def main():

    pass

if __name__ == '__main__':
    main()

# print vector(1,1,1).clockwise(2)
# myFunTest(circle(point(1,1),-32).offset, 2, goal="goal")
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
# myFunTest(circle(point(1,1), 10).move, vector(1,1) , goal="goal")

# print X.move(vector(1, 1))
# X.move(vector(1,1))
# print X.db
# print X

# myFunTest(point2d(1,1).move, vector(2,2), goal="goal")
# v=vector(1,1,1)
# o=vector(1,1)
# p=point2d(1,1)
# print p.move(o)
# p.move(o)
# print p.move(v)
# p.move(v)
# print X.remove(point(2,2,2)).length
# print X.length
# print (X | Y).length
# print X.length

# help(X)
# print x.length, y.length, z.length
# x = Models({line(point2d(0, 0), point2d(1, 1),), point(
#     0, 0), point(2, 2, 2), circle(point(4, 2), 20)})
# y = Models({point(0, 0)})

# z = Models({lwpolyline(point(0, 0), point(0, 0), point(2, 1))})
# print x.length
# x -= y
# print x.length
# print fun(vector.clockwise, (2,3,4))
# print vector.__class__.__name__
# print tail_call_optimized.__class__.__name__
# print vector.clockwise.__class__.__name__
# for i in range(0,8):
# p1 = point(0,0,0)
# p2 = point(1,1,1)
# p3 = point(1,1,0)
# P1 = Point(0,0,0)
# P2 = Point(1,1,1)
# P3 = Point(1,1,0)
# myFunTest(line(p1, p2).offset, 10, goal="goal")
# print vector(1,0).clockwise()
# myFunTest(line(p1, p2).angle_between, line(p1, p3), goal="goal")
# from sympy import Point, Line
# l1 = line(p1, p2)
# l2 = line(p4, p5)
# a = eval(l1.intersection(l2)[0].__repr__().lower())
# print point2d(15/8, 15/8)

# print point(1,1).sympy
# print circle(point(2,2), 10).sympy()
# circle 貌似不行 intersection 要分别写
# print vector(1,0).rotate2d(math.pi/2)

# print eval(sympy2m(Point(1,1,1)))

# print lwpolyline(p1, p2, p3, p4).offset(0.5)
# lwpolyline(point2d(0.35355339059327373,-0.35355339059327373),point2d(0.17485923006355816,-0.5322475511229905),point2d(-0.1180339887498931,-1.1180339887498945),point2d(3.223606797749979,0.5527864045000421))

# lwpolyline(point2d(0.07071067811865475,-0.07071067811865475),point2d(1.634971846012718,1.493550489775416),point2d(0.7763932022500191,-0.223606797749982),point2d(3.044721359549996,0.9105572809000084))
# print lwpolyline(p1,p2,p3,p4).offset(-0.1)
# lwpolyline(point2d(-0.07071067811865475,0.07071067811865475),point2d(2.365028153987279,2.506449510224577),point2d(1.2236067977499774,0.22360679774997833),point2d(2.955278640450004,1.0894427190999916))
# print vector(0,-1).slope * -1

# a = Models()
# print a

# a = lwpolyline(point(1,1), point(2,2), point(3,3))
# print a.sympy
p1, p2, = point(0, 0), point(0, 10000)
p3, p4 = point(-5000, 5000), point(5000, 5000)
p5 = point(2, 0)
# a = lwpolyline(p1, p2, p3, p2, p4)
# print a.offset(-0.1)
# print a.intersection(line(point(0,1), point(1,0)))
# lwpolyline(point2d(0.0,0.1),point2d(0.9,0.1),point2d(0.9,1.0),point2d(1.1,0.0),point2d(1.0,0.0))
# a = Models([p1])
# b = Models([p2])
# a ^= b
# print a
# print b
# print line(p1, p2).merge(line(p3, p4))
# print p1.copy() == p1
# print Models([p1,p2,p3])
w1 = wall(line(p1, p2))
w2 = wall(line(p3, p4))
print w1.merge(w2)
# print w1.base.sympy
# 
# Models([
#     line(point2d(0, 0),point2d(0, 5000)),
# line(point2d(0, 10000),point2d(0, 5000)),
# line(point2d(-5000, 5000),point2d(0, 5000)),
# line(point2d(5000, 5000),point2d(0, 5000))])
