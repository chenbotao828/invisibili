# coding=utf-8
from __future__ import division
from core import _const, myFunTest, myProTest, typeTest


"define const data"
const = _const()

"type of numbers"
num = const.Num = [int, float, long]

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


class wall(myObject):
    '''a wall defined by a '''

    def __init__(self, arg):

        typeTest([typeList], arg)
        self.args = (arg)
        self.arg = arg

myProTest(Point(3, 4).xx, 3)
