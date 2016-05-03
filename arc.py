# coding=utf-8
from model import *

class wall(model.myObject):
    '''wall object, line base'''

    def __init__(self, base, lwidth=100, rwidth=100, hight=3000):

        typeTest([line, const.N, const.N, const.N],
                 base, lwidth, rwidth, hight)
        self.para = ("base", "lwidth", "rwidth", "hight")
        self.base = base
        self.lwidth = lwidth
        self.rwidth = rwidth
        self.hight = hight

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
        il = self.base.sympy.intersection(another.base.sympy)
        if il == []:
            ret = Models([self, another])
        elif isinstance(il[0], Segment):
            if self.args[1:] == another.args[1:]:
                new_base = self.base.merge(another.base)
                ret = Models([self.set_attr(base=new_base)])
            else:
                raise Exception("Two kinds of walls overlapped")
        elif isinstance(il[0], Point):
            ip = eval(sympy2m(il[0]))
            p_set = Models([ip, self.base.p1, self.base.p2,
                            another.base.p1, another.base.p2])
            p_set.remove(ip)
            ret = Models()
            for p in p_set:
                # ret.add(line(p, ip))
                if p in self.base.args:
                    ret.add(self.set_attr(base=line(p, ip)))
                if p in another.base.args:
                    ret.add(another.set_attr(base=line(p, ip)))

        return ret
