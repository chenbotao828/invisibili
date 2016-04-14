# coding=utf-8
from __future__ import division

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


class mVector(myObject):
    '''my simple 2D vector, tuple of 2 num'''

    def __init__(self, i, j):
        typeTest([(int, float, long)] * 2, i, j)
        self.i = i
        self.j = j
        self.args = (i, j)


class mPoint(myObject):
    '''my simple 2D point'''

    def __init__(self, x, y):

        typeTest([const.Num] * 2, x, y)
        self.args = (x, y)
        self.x = x
        self.y = y


class mSegPoint(myObject):
    '''a parametric 2D point in a segment
    zero length segment return a 2D Point
    '''

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


class mSwall(myObject):
    '''my simple straight wall from a segment'''

    def __init__(self, seg, attDict={}):

        typeTest([mSegment, dict], seg, attDict)
        self.args = (seg, attDict)
        self.seg = seg
        self.attDict = attDict


class mSegment(myObject):
    '''my simple 2d segment, p1 is nearer to origin than p2'''

    def __init__(self, p1, p2):

        typeTest([mPoint] * 2, p1, p2)
        if point2origin(p2) < point2origin(p1):
            p1, p2 = p2, p1
        self.args = (p1, p2)
        self.p1 = p1
        self.p2 = p2


class linearEquation(myObject):
    '''y = ax + b for x in xSpan'''

    def __init__(self, a, b, xSpan):

        typeTest([const.Num, const.Num, mSpan], a, b, xSpan)
        self.args = (a, b, xSpan)
        self.a = a
        self.b = b
        self.xSpan = xSpan


class vtclinearEquation(myObject):
    '''x = c for y in ySpan'''

    def __init__(self, c, ySpan):

        typeTest([const.Num, mSpan], c, ySpan)
        self.args = (c, ySpan)
        self.c = c
        self.ySpan = ySpan


class mSpan(myObject):
    '''a <= x <= b'''

    def __init__(self, a, b):

        typeTest([const.Num] * 2, a, b)
        if a > b:
            a, b = b, a
        self.args = (a, b)
        self.a = a
        self.b = b


class mWallset(myObject):
    '''wall set'''

    def __init__(self, *swalls):

        typeTest([const.Wall] * len(swalls), *swalls)
        self.args = swalls
        self.swalls = list(swalls)

'''
-------------------------------------------------------------------------------
Const data of invisibili
-------------------------------------------------------------------------------
'''


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
const.Num = [int, float, long]
const.Wall = [mSwall]

'''
-------------------------------------------------------------------------------
Functions of invisibili
-------------------------------------------------------------------------------
'''


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
    if not (ret == goal) or type(ret) == Exception:
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
        raise Warning("%s Error" % fun.__name__)


def isNum(value):
    '''return True if value is int, float ...'''
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True


def vectorLength(aVector):
    '''return length of a vector'''
    typeTest([mVector], aVector)
    return (aVector.i**2 + aVector.j**2)**0.5


def unitVector(aVector):
    '''return unit vector, (0,0) returns itself'''
    typeTest([mVector], aVector)
    if aVector == mVector(0, 0):
        return aVector
    else:
        l = vectorLength(aVector)
        i = aVector.i / l
        j = aVector.j / l
        return mVector(i, j)


def clwVector(aVector):
    '''return 90 degree clockwise of the vector'''

    typeTest([mVector], aVector)
    return mVector(aVector.j, -aVector.i)


def reverseVector(aVector):
    '''return a reversed vector'''

    typeTest([mVector], aVector)
    return mVector(-aVector.i, -aVector.j)


def disclwVector(aVector):
    '''return 90 degree disclockwise vector'''

    typeTest([mVector], aVector)
    return reverseVector(clwVector(aVector))


def segEquation(aSeg):
    '''return linear equation object of a segment'''

    typeTest([mSegment], aSeg)
    if aSeg.p1.x == aSeg.p2.x:
        y1 = aSeg.p1.y
        y2 = aSeg.p2.y
        ySpan = mSpan(y1, y2)
        return vtclinearEquation(aSeg.p1.x, ySpan)
    else:
        a = (aSeg.p1.y - aSeg.p2.y) / (aSeg.p1.x - aSeg.p2.x)
        b = aSeg.p1.y - a * aSeg.p1.x
        x1 = aSeg.p1.x
        x2 = aSeg.p2.x
        xSpan = mSpan(x1, x2)
        return linearEquation(a, b, xSpan)


def point2origin(aPoint):
    '''return distance between a 2D point to origin'''

    typeTest([mPoint], aPoint)
    return (aPoint.x ** 2 + aPoint.y ** 2) ** 0.5


def segSlope(aSeg):
    '''return slope of a segment'''

    typeTest([mSegment], aSeg)
    if type(segEquation(aSeg)) == vtclinearEquation:
        return float("inf")
    else:
        return segEquation(aSeg).a


def isIntersectSpan(span1, span2):
    '''return True if a span intersect another'''

    typeTest([mSpan] * 2, span1, span2)
    if span1.b < span2.a or span2.b < span1.a:
        return False
    return True


def numInSpan(num, aSpan):
    '''return True if a num is in a range '''

    typeTest([const.Num, mSpan], num, aSpan)
    if aSpan.a <= num <= aSpan.b:
        return True
    return False


def isIntersectSeg(seg1, seg2):
    '''return True if a segment intersect another'''

    typeTest([mSegment] * 2, seg1, seg2)
    if segSlope(seg1) == segSlope(seg2) == float("inf"):
        c1, ySpan1 = segEquation(seg1).args
        c2, ySpan2 = segEquation(seg2).args
        if c1 == c2 and isIntersectSpan(ySpan1, ySpan2):
            return True
        else:
            return False
    elif float("inf") in map(segSlope, [seg1, seg2]):
        if segSlope(seg1) == float("inf"):
            seg1, seg2 = seg2, seg1
        a, b, xSpan = segEquation(seg1).args
        c, ySpan = segEquation(seg2).args
        y = a * c + b
        if numInSpan(y, ySpan) and numInSpan(c, xSpan):
            return True
        return False
    else:
        a1, b1, xSpan1 = segEquation(seg1).args
        a2, b2, xSpan2 = segEquation(seg2).args
        if a1 == a2:
            if b1 == b2 and isIntersectSpan(xSpan1, xSpan2):
                return True
            return False
        else:
            x = (b2 - b1) / (a1 - a2)
            if numInSpan(x, xSpan1) and numInSpan(x, xSpan2):
                return True
            return False


def unionSpan(span1, span2):
    '''return union of two span if intersected'''

    typeTest([mSpan] * 2, span1, span2)
    if not isIntersectSpan(span1, span2):
        return None
    else:
        l = [span1.a, span1.b, span2.a, span2.b]
        a = min(l)
        b = max(l)
        return mSpan(a, b)


def intersectSpan(span1, span2):
    '''return intersection of two span if intersected'''

    typeTest([mSpan] * 2, span1, span2)
    if not isIntersectSpan(span1, span2):
        return None
    else:
        a, b = span1.args
        c, d = span2.args
        if numInSpan(c, span1) and numInSpan(d, span1):
            return span2
        elif numInSpan(c, span1):
            return mSpan(c, b)
        elif numInSpan(d, span1):
            return mSpan(a, d)
    return None


def jointSeg(seg1, seg2):
    '''return Joint segment of two segments, if collinear and adjacent'''

    typeTest([mSegment] * 2, seg1, seg2)
    if segSlope(seg1) == segSlope(seg2) and\
            type(segIntersectPoint(seg1, seg2)) == mPoint:
        eq1 = segEquation(seg1)
        eq2 = segEquation(seg2)
        if segSlope(seg1) == float('inf'):
            return equation2seg(
                vtclinearEquation(eq1.c, unionSpan(eq1.ySpan, eq2.ySpan)))
        else:
            return equation2seg(
                linearEquation(eq1.a, eq1.b, unionSpan(eq1.xSpan, eq2.xSpan)))
    else:
        return None


def linearEquationY(linearEq, x):
    '''given linear equation and X return Y or Y span'''

    typeTest([[linearEquation, vtclinearEquation], const.Num], linearEq, x)
    if type(linearEq) == vtclinearEquation:
        if x == linearEq.c:
            return linearEq.ySpan
        else:
            return None
    if type(linearEq) == linearEquation:
        a, b, xSpan = linearEq.args
        if not numInSpan(x, xSpan):
            return None
        else:
            return x * a + b


def equation2seg(aLinearEq):
    '''return segment of a linear equation  '''

    typeTest([[linearEquation, vtclinearEquation]], aLinearEq)
    if type(aLinearEq) == linearEquation:
        xSpan = aLinearEq.xSpan
        p1 = mPoint(xSpan.a, linearEquationY(aLinearEq, xSpan.a))
        p2 = mPoint(xSpan.b, linearEquationY(aLinearEq, xSpan.b))
        return mSegment(p1, p2)
    if type(aLinearEq) == vtclinearEquation:
        c, ySpan = aLinearEq.args
        p1 = mPoint(c, ySpan.a)
        p2 = mPoint(c, ySpan.b)
        return mSegment(p1, p2)


def segIntersectPoint(seg1, seg2):
    '''return intection point of two segments ,
    if overlapped return parametric point
    '''

    typeTest([mSegment] * 2, seg1, seg2)
    if not isIntersectSeg(seg1, seg2):
        return None
    if segSlope(seg1) == segSlope(seg2) == float("inf"):
        c1, ySpan1 = segEquation(seg1).args
        c2, ySpan2 = segEquation(seg2).args
        newSpan = intersectSpan(ySpan1, ySpan2)
        return mSegPoint(
            mSegment(mPoint(c1, newSpan.a), mPoint(c1, newSpan.b)))
    elif float("inf") in map(segSlope, [seg1, seg2]):
        if segSlope(seg1) == float("inf"):
            seg1, seg2 = seg2, seg1
        a, b, xSpan = segEquation(seg1).args
        c, ySpan = segEquation(seg2).args
        x = c
        y = a * c + b
        return mPoint(x, y)
    else:
        a1, b1, xSpan1 = segEquation(seg1).args
        a2, b2, xSpan2 = segEquation(seg2).args
        if a1 == a2:
            newSpan = intersectSpan(xSpan1, xSpan2)
            p1 = mPoint(newSpan.a, a1 * newSpan.a + b1)
            p2 = mPoint(newSpan.b, a1 * newSpan.b + b1)
            return mSegPoint(mSegment(p1, p2))
        else:
            x = (b2 - b1) / (a1 - a2)
            y = a1 * x + b1
            return mPoint(x, y)


def intersectSeg(seg1, seg2):
    '''return list of intersected segments'''

    typeTest([mSegment] * 2, seg1, seg2)

    if not isIntersectSeg(seg1, seg2):
        return [seg1, seg2]
    ip = segIntersectPoint(seg1, seg2)
    if type(ip) == mSegPoint:
        raise Exception("<%s> and <%s> is overlapped!" %
                        (seg1, seg2))
    if type(ip) == mPoint:
        if ip in seg1.args and ip in seg2.args:
            return [seg1, seg2]
        if ip in seg1.args or ip in seg2.args:
            if ip in seg1.args:
                seg1, seg2 = seg2, seg1
            seg3 = mSegment(seg1.p1, ip)
            seg4 = mSegment(ip, seg1.p2)
            return [seg2, seg3, seg4]
        else:
            return [mSegment(seg1.p1, ip),
                    mSegment(ip, seg1.p2),
                    mSegment(seg2.p1, ip),
                    mSegment(ip, seg2.p2)]


def intersectSwall(sw1, sw2):
    '''return list of straight walls'''

    typeTest([mSwall] * 2, sw1, sw2)
    seg1 = sw1.seg
    seg2 = sw2.seg

    segList = intersectSeg(seg1, seg2)
    if len(segList) == 2:
        return [sw1, sw2]
    ip = segIntersectPoint(seg1, seg2)
    if len(segList) == 3:
        if ip in seg1.args:
            seg1, seg2 = seg2, seg1
            sw1, sw2 = sw2, sw1
            sw3 = mSwall(segList[1], sw1.attDict)
            sw4 = mSwall(segList[2], sw1.attDict)
            return [sw2, sw3, sw4]
    if len(segList) == 4:
        return [mSwall(mSegment(seg1.p1, ip), sw1.attDict),
                    mSwall(mSegment(ip, seg1.p2), sw1.attDict),
                    mSwall(mSegment(seg2.p1, ip), sw2.attDict),
                    mSwall(mSegment(ip, seg2.p2), sw2.attDict)]
    # if not isIntersectSeg(seg1, seg2):
    #     return [sw1, sw2]

    # ip = segIntersectPoint(seg1, seg2)
    # if type(ip) == mSegPoint:
    #     raise Exception("<%s> and <%s> is overlapped!" %
    #                     (sw1, sw2))

    # if type(ip) == mPoint:
    #     if ip in seg1.args and ip in seg2.args:
    #         return [sw1, sw2]
    #     if ip in seg1.args or ip in seg2.args:
    #         if ip in seg1.args:
    #             seg1, seg2 = seg2, seg1
    #             sw1, sw2 = sw2, sw1
    #         sw3 = mSwall(mSegment(seg1.p1, ip), sw1.attDict)
    #         sw4 = mSwall(mSegment(ip, seg1.p2), sw1.attDict)
    #         return [sw2, sw3, sw4]
    #     else:
    #         return [mSwall(mSegment(seg1.p1, ip), sw1.attDict),
    #                 mSwall(mSegment(ip, seg1.p2), sw1.attDict),
    #                 mSwall(mSegment(seg2.p1, ip), sw2.attDict),
    #                 mSwall(mSegment(ip, seg2.p2), sw2.attDict)]


# def addSwall(aSwall, aWallset):
#     '''return a wall set, a swall added'''

#     typeTest([mSwall, mWallset], aSwall, aWallset)
#     for anotherSwall in aWallset.swalls:
#         if rectOverlapped(inRect(aSwall), inRect(anotherSwall)):
#             if isIntersectSeg(aSwall.seg, anotherSwall.seg):
#                 pass

# myFunTest(addSwall, goal, args)


# def wallsetSeg(aWallset):
#     '''return list of segments of wall set'''

#     typeTest([mWallset], aWallset)


# myFunTest(wallsetSeg, goal, args)

'''
-------------------------------------------------------------------------------
unit test of invisibili
-------------------------------------------------------------------------------
'''
if __name__ == '__main__':
    myFunTest(intersectSeg,
              [mSegment(mPoint(0.5, 0.5), mPoint(0, 1)), mSegment(mPoint(0.5, 0.5), mPoint(1, 0)), mSegment(mPoint(
                  0, 0), mPoint(0.5, 0.5)), mSegment(mPoint(0.5, 0.5), mPoint(1, 1))], mSegment(mPoint(0, 1), mPoint(1, 0)),
              mSegment(mPoint(0, 0), mPoint(1, 1)))
    equation2segGoal = mSegment(mPoint(3, 0), mPoint(3, 1))
    myFunTest(equation2seg, equation2segGoal,
              vtclinearEquation(3, mSpan(0, 1)))

    myFunTest(linearEquationY, 0.2, linearEquation(1, 0, mSpan(0, 1)), 0.2)
    myFunTest(segIntersectPoint,
              mPoint(-0.5, -0.5),
              mSegment(mPoint(0, 0), mPoint(-1, -1)),
              mSegment(mPoint(0, -1), mPoint(-1, 0)))
    myFunTest(intersectSpan, mSpan(2, 2), mSpan(1, 2), mSpan(2, 3))
    myFunTest(numInSpan, False, -1, mSpan(0, 2))
    myFunTest(segSlope, 1, mSegment(mPoint(0, 0), mPoint(2, 2)))
    myFunTest(isIntersectSpan, False, mSpan(0, -1.2), mSpan(1, 2))
    myFunTest(unionSpan, mSpan(1, 9.0), mSpan(1, 3), mSpan(2, 9))
    myFunTest(segIntersectPoint, None, mSegment(mPoint(0, 1), mPoint(0, 2)),
              mSegment(mPoint(1, 1), mPoint(2, 2)))
    myFunTest(isIntersectSeg, False, mSegment(mPoint(0, 1), mPoint(0, 2)),
              mSegment(mPoint(1, 1), mPoint(2, 2)))
    myFunTest(isIntersectSeg, True, mSegment(mPoint(0, 0), mPoint(1, 1)),
              mSegment(mPoint(1, 1), mPoint(3, 3)))
    myFunTest(isIntersectSeg, True, mSegment(mPoint(1, 0), mPoint(1, 1)),
              mSegment(mPoint(1, 0), mPoint(1, 1)))
    myFunTest(unitVector, mVector(1, 0), mVector(3, 0))
    myFunTest(clwVector, mVector(1, 0), mVector(0, 1))
    myFunTest(reverseVector, mVector(1, 1), mVector(-1, -1))
    myFunTest(disclwVector, mVector(-1, 0), mVector(0, 1))
    myFunTest(vectorLength, 5, mVector(3, 4))
    myFunTest(point2origin, 5, mPoint(3, 4))

    '''raise Exception: swalls is overlapped'''
    # sw1 = mSwall(mPoint(1, 1), mPoint(0, 0))
    # sw2 = mSwall(mPoint(1, 1), mPoint(0.5, 0.5))
    # myFunTest(intersectSwall, "", sw1, sw2)
    # intersectSwall(sw1, sw2)
    # seg1 = mSegment(mPoint(2, 2), mPoint(1, 1))
    # seg2 = mSegment(mPoint(1, 1), mPoint(3, 3))
    # myFunTest(jointSeg, mSegment(mPoint(1, 1), mPoint(3, 3)),
    #           seg1,
    #           seg2)
    sw1 = mSwall(mSegment(mPoint(0, 0), mPoint(1, 1)))
    sw2 = mSwall(mSegment(mPoint(2, 2), mPoint(3, 3)))
    myFunTest(intersectSwall, [sw1, sw2], sw1, sw2)
    sw3 = mSwall(mSegment(mPoint(0.5, 0.5), mPoint(1, 1)))
    # myFunTest(intersectSwall,[sw1, sw3], sw1, sw3)
    sw4 = mSwall(mSegment(mPoint(2, 2), mPoint(1, 1)))
    myFunTest(intersectSwall, [sw1, sw4], sw1, sw4)
    sw5 = mSwall(mSegment(mPoint(1, 0), mPoint(0.5, 0.5)))
    sw6 = mSwall(mSegment(mPoint(0, 0), mPoint(0.5, 0.5)))
    sw7 = mSwall(mSegment(mPoint(1, 1), mPoint(0.5, 0.5)))
    # myFunTest(intersectSwall, [sw5, sw7, sw6, ], sw1, sw5)
    sw8 = mSwall(mSegment(mPoint(0, 1), mPoint(1, 0)), {1:1})
    sw9 = mSwall(mSegment(mPoint(0.5, 0.5), mPoint(0, 1)))
    # myFunTest(intersectSwall, [sw7,sw5,sw6,sw9],  sw8,sw1)
    w1 = mSwall(mSegment(mPoint(0, 2), mPoint(1, 0)))
    w2 = mSwall(mSegment(mPoint(0, 0), mPoint(1, 2)))
    w3 = mSwall(mSegment(mPoint(1, 0), mPoint(0.5, 1.0)), {})
    w4 = mSwall(mSegment(mPoint(0.5, 1.0), mPoint(0, 2)), {})
    w5 = mSwall(mSegment(mPoint(0, 0), mPoint(0.5, 1.0)), {})
    w6 = mSwall(mSegment(mPoint(0.5, 1.0), mPoint(1, 2)), {})
    # myFunTest(intersectSwall, [w3, w4, w5, w6],  w2, w1)
