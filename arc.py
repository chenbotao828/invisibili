# coding=utf-8
from __future__ import division
from model import *


class wall(myObject):
    '''wall object, line base'''

    def __init__(self, base, lwidth=100, rwidth=100, hight=3000,
                 material="brick"):

        typeTest([line, Num.const, Num.const, Num.const],
                 base, lwidth, rwidth, hight)
        self.para = ("base", "lwidth", "rwidth", "hight")
        self.base = base
        self.lwidth = lwidth
        self.rwidth = rwidth
        self.hight = hight
        self.material = material

    def outline(self):
        '''return Models object contains wall's sides and ends'''

        left = self.base.offset(-lwidth)
        right = (self.base.offset(rwidth))
        top = line(left.p1, right.p1)
        bottom = line(left.p2, right.p2)
        return Models([left, right, top, bottom])

    def merge(self, another):
        '''merge a wall with another wall, return Models set'''

        typeTest([wall], another)
        if self == another:
            ret = [self]
        il = self.base.sympy.intersection(another.base.sympy)
        if il == []:
            ret = [self, another]
        elif isinstance(il[0], Segment):
            if self.args[1:] == another.args[1:]:
                new_base = self.base.merge(another.base)
                ret = [self.with_attr(base=new_base)]
            else:
                raise Exception("Two diffrent walls overlapped")
        elif isinstance(il[0], Point):
            ip = eval(sympy2m(il[0]))
            p_set = Models([ip, self.base.p1, self.base.p2,
                            another.base.p1, another.base.p2])
            p_set.remove(ip)
            ret = []
            for p in p_set:
                if p in self.base.args:
                    ret.append(self.with_attr(base=line(p, ip)))
                if p in another.base.args:
                    ret.append(another.with_attr(base=line(p, ip)))
        return ret
