# coding=utf-8
from __future__ import division
import sys

class _const(object):
    "const class"

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise Warning("Const Error")
        else:
            self.__dict__[key] = value

"define const data"
const = _const()

"type of numbers"
const.typeNum = [int, float, long]


def myFunTest(fun, goal, *args):
    '''report errors if function is failed'''
    import datetime
    ret = "DEFAULT"
    if type(fun).__name__ != 'function':
        error = "1st parameter expect a function(" \
            + type(fun).__name__ + " given)"
        raise TypeError(error)
    startTime = datetime.datetime.now()
    ret = fun(*args)
    endTime = datetime.datetime.now()
    if not (ret == goal):
        get_cur_info()
        firstLineStr = "Function Error: \"%s\"" % fun.__name__
        l = (79 - len(firstLineStr)) // 2
        print("-" * l + firstLineStr + "-" * l)
        print(("FAIL: " + fun.__name__ +
               str(args) + " = " + str(ret)) +
              " (type: " + type(ret).__name__ + ")")
        print(("GOAL: " + str(goal)))
        lastLineStr = "Run time: %s" % (endTime - startTime)
        l = (79 - len(lastLineStr)) // 2
        print("-" * l + lastLineStr + "-" * l)


def typeTest(typeList, *args):
    '''Type test of args inside a function or a class'''
    l1 = len(typeList)
    l2 = len(args)
    if l1 != l2:
        raise IndexError("len(typeList) != len(args) (%d != %d)" % (l1, l2))
    for i in range(l1):
        if type(typeList[i]) in [list, tuple]:
            if type(args[i]) not in typeList[i]:
                raise TypeError("%dth parameter expect %s, given %s \"%s\"" %
                                (i + 1, str([x.__name__ for x in typeList[i]]),
                                 type(args[i]).__name__, str(args[i])))
        elif type(args[i]) != typeList[i]:
            raise TypeError("%dth parameter expect %s, given %s \"%s\"" %
                            (i + 1, typeList[i].__name__,
                                type(args[i]).__name__, str(args[i])))


class myObject(object):
    "modified Object"

    def __init__(self, *args):
        pass

    def __repr__(self):
        if type(self.args) != tuple:
            return type(self).__name__ + "(" + str(self.args) + ")"
        return type(self).__name__ + str(self.args)

    def __eq__(self, anonther):
        if type(self) == type(anonther) and self.__dict__ == anonther.__dict__:
            return True
        return False


class mSegment(myObject):
    '''my simple 2d segment'''

    def __init__(self, p1, p2):

        typeTest([mPoint] * 2, p1, p2)
        self.args = (p1, p2)
        self.p1 = p1
        self.p2 = p2


class mPoint(myObject):
    '''my simple 2D point'''

    def __init__(self, x, y):

        typeTest([const.typeNum] * 2, x, y)
        self.args = (x, y)
        self.x = x
        self.y = y


class mParaPoint(myObject):
    '''a parametric 2D point in a segment'''

    def __init__(self, seg):

        typeTest([mSegment], seg)
        self.args = (seg)
        self.seg = seg
        if seg.p1 == seg.p2:
            self.__class__ = mPoint
            self.args = (seg.p1.x, seg.p1.y)
            self.x = seg.p1.x
            self.y = seg.p1.y
            del self.seg

# c = mParaPoint(mSegment(mPoint(1, 1), mPoint(1, 1)))
# print dir(c)
# print "-"*79
# print c.__hash__()
# print hash(c)
# print "-"*79
# print c.__dict__
p1 = mPoint(1.0,2)
p2 = mPoint(2.0,3)
print mS
