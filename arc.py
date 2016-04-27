# coding=utf-8
from model import *

class Wall(myObject):
    '''Wall object'''

    def __init__(self, base, lwidth=100, rwidth=100, hight=3000):

        typeTest([Models, Num, Num, Num], base, lwidth, rwidth, hight)
        self.args = (base, lwidth, rwidth, hight)
        self.base = base
        self.lwidth = lwidth
        self.rwidth = rwidth
        self.hight = hight

    def outline(self):
        '''return Models'''

        ret = Models()
        for m in base:
            try:
                left = m.offset()
            except:
                pass

