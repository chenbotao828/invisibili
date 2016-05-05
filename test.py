# coding=utf-8
from __future__ import division
from model import *
from arc import * 
import draw

p1, p2, = point(0, 0), point(0, 1)
p3, p4 = point(-1, 0), point(1, 0)
p5 = point(2, 2)


# w1 = wall(line(p1, p2), hight = 1200)
# w2 = wall(line(p3, p4))
# print w1.merge(w2)
# ws = Models([w1, w2])
# print ws
# print ws
# print map(lambda x: Models(w1.merge(x)), {w2})
# print ws.merge_walls()
m = Models([lwpolyline(p1,p2,p5)])
draw.draw_Models(m)
