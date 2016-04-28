# coding=utf-8
from model import *
from arc import *


def main():

    pass

if __name__ == '__main__':
    main()

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
x = Models({line(point2d(0, 0), point2d(1, 1),), point(
    0, 0), point(2, 2, 2), circle(point(4, 2), 20)})
y = Models({point(0, 0)})

z = Models({lwpolyline(point(0, 0), point(0, 0), point(2, 1))})
print x.length
x -= y
print x.length
