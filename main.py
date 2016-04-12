# coding=utf-8
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
const.typeNum = [int, float, long]


'''
-------------------------------------------------------------------------------
Models of invisibili
-------------------------------------------------------------------------------
'''


class mObject(object):
    "modified Object"

    def __init__(self, *args):
        pass

    def __str__(self):
        return type(self).__name__ + str(self.args)

    def __eq__(self, anonther):
        if type(self) == type(anonther) and self.args == anonther.args:
            return True
        return False


class mVector(mObject):
    '''my simple 2D vector, tuple of 2 num'''

    def __init__(self, i, j):
        typeTest([(int, float, long)] * 2, i, j)
        self.i = i
        self.j = j
        self.args = (i, j)


class mPoint(mObject):
    '''my simple 2D point'''

    def __init__(self, x, y):

        typeTest([const.typeNum] * 2, x, y)
        self.args = (x, y)
        self.x = x
        self.y = y


class mParaPoint(mObject):
    '''a parametric 2D point in a segment'''

    def __init__(self, seg):

        typeTest([mSegment], seg)
        self.args = (seg)
        self.seg = seg


class mSwall(mObject):
    '''my simple straight wall'''

    def __init__(self, start, end, lw=100, rw=100, attDict={}):

        typeTest([mPoint, mPoint, const.typeNum, const.typeNum, dict],
                 start, end, lw, rw, attDict)
        self.args = (start, end, lw, rw, attDict)
        self.start = start
        self.end = end
        self.lw = lw
        self.rw = rw
        self.attDict = attDict


class mSegment(mObject):
    '''my simple 2d segment'''

    def __init__(self, p1, p2):

        typeTest([mPoint, mPoint], p1, p2)
        self.args = (p1, p2)
        self.p1 = p1
        self.p2 = p2


class linearEquation(mObject):
    '''y = ax + b for x in [xMin, xMax]'''

    def __init__(self, a, b, xMin, xMax):

        typeTest([const.typeNum] * 4, a, b, xMin, xMax)
        self.args = (a, b, xMin, xMax)
        self.a = a
        self.b = b
        self.xMin = xMin
        self.xMax = xMax


class vtclinearEquation(mObject):
    '''x = c for y in[yMin, yMax]'''

    def __init__(self, c, yMin, yMax):

        typeTest([const.typeNum] * 3, c, yMin, yMax)
        self.args = (c, yMin, yMax)
        self.c = c
        self.yMin = yMin
        self.yMax = yMax


class mSpan(mObject):
    '''a <= x <= b'''

    def __init__(self, a, b):

        typeTest([const.typeNum] * 2, a, b)
        if a > b:
            a, b = b, a
        self.args = (a, b)
        self.a = a
        self.b = b


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
    if not (ret == goal):
        firstLineStr = "Function Error: \"%s\"" % fun.__name__
        l = (79 - len(firstLineStr)) // 2
        print("-" * l + firstLineStr + "-" * l)
        print(("FAIL: " + fun.__name__ +
              str(args) + " = " + str(ret)) +\
            " (type: " + type(ret).__name__ + ")")
        print(("GOAL: " + str(goal)))
        lastLineStr = "Run time: %s" % (endTime - startTime)
        l = (79 - len(lastLineStr)) // 2
        print("-" * l + lastLineStr + "-" * l)


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
        yMin = min(y1, y2)
        yMax = max(y1, y2)
        return vtclinearEquation(aSeg.p1.x, yMin, yMax)
    else:
        a = (aSeg.p1.y - aSeg.p2.y) / (aSeg.p1.x - aSeg.p2.x)
        b = aSeg.p1.y - a * aSeg.p1.x
        x1 = aSeg.p1.x
        x2 = aSeg.p2.x
        xMin = min(x1, x2)
        xMax = max(x1, x2)
        return linearEquation(a, b, xMin, xMax)


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

    typeTest([const.typeNum, mSpan], num, aSpan)
    if aSpan.a <= num <= aSpan.b:
        return True
    return False


def isIntersectSeg(seg1, seg2):
    '''return True if a segment intersect anonther'''

    typeTest([mSegment] * 2, seg1, seg2)
    if segSlope(seg1) == segSlope(seg2) == float("inf"):
        c1, yMin1, yMax1 = segEquation(seg1).args
        c2, yMin2, yMax2 = segEquation(seg2).args
        if c1 == c2 and isIntersectSpan(
                mSpan(yMin1, yMax1), mSpan(yMin2, yMax2)):
            return True
        else:
            return False
    elif float("inf") in map(segSlope, [seg1, seg2]):
        if segSlope(seg1) == float("inf"):
            seg1, seg2 = seg2, seg1
        a, b, xMin, xMax = segEquation(seg1).args
        c, yMin, yMax = segEquation(seg2).args
        y = a * c + b
        if numInSpan(y, mSpan(yMin, yMax)) and \
                numInSpan(c, mSpan(xMin, xMax)):
            return True
        return False
    else:
        a1, b1, xMin1, xMax1 = segEquation(seg1).args
        a2, b2, xMin2, xMax2 = segEquation(seg2).args
        if a1 == a2:
            if b1 == b2 and isIntersectSpan(
                    mSpan(xMin1, xMax1), mSpan(xMin2, xMax2)):
                return True
            return False
        else:
            x = (b2 - b1) / (a1 - a2)
            if numInSpan(x, mSpan(xMin1, xMax1)) and \
                    numInSpan(x, mSpan(xMin2, xMax2)):
                return True
            return False


def unionSpan(span1, span2):
    '''return joint of two span if intersected'''

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

myFunTest(intersectSpan, None, mSpan(1, 2), mSpan(2, 3))


def segIntersectPoint(seg1, seg2):
    '''return intection Point of two segment'''

    typeTest([mSegment] * 2, seg1, seg2)
    if not isIntersectSeg(seg1, seg2):
        return None
    else:
        if segSlope(seg1) == segSlope(seg2) == float("inf"):
            c1, yMin1, yMax1 = segEquation(seg1).args
            c2, yMin2, yMax2 = segEquation(seg2).args
            l = [yMin1, yMax1, yMin2, yMax2]
            yMin = min(l)
            yMax = max(l)
            return mParaPoint(mSegment(mPoint(c1, yMin), mPoint(c1, yMax)))
        elif float("inf") in map(segSlope, [seg1, seg2]):
            if segSlope(seg1) == float("inf"):
                seg1, seg2 = seg2, seg1
            a, b, xMin, xMax = segEquation(seg1).args
            c, yMin, yMax = segEquation(seg2).args
            x = c
            y = a * c + b
            return mPoint(x, y)
        else:
            a1, b1, xMin1, xMax1 = segEquation(seg1).args
            a2, b2, xMin2, xMax2 = segEquation(seg2).args
            if a1 == a2:
                l = [xMin1, xMax1, xMin2, xMax2]
                xMin = min(l)
                xMax = max(l)

                # if b1 == b2 and isIntersectSpan(
                #         mSpan(xMin1, xMax1), mSpan(xMin2, xMax2)):
                #     return True
                # return False
            else:
                x = (b2 - b1) / (a1 - a2)
                if numInSpan(x, mSpan(xMin1, xMax1)) and \
                        numInSpan(x, mSpan(xMin2, xMax2)):
                    return True
                return False


# def intersectSwall(s1, s2):
#     '''return intersection of two Swalls, swall list'''

#     typeTest([swall, swall], s1, s2)
#     if isIntersect((s1.start, s1.end), (s2.start, s2.end)):
#         ip = intersectionPoint((s1.start, s1.end), (s2.start, s2.end))

'''
-------------------------------------------------------------------------------
unit test of invisibili
-------------------------------------------------------------------------------
'''

# myFunTest(numInSpan, False, -1, mSpan(0, 2))
# myFunTest(segSlope, 1, mSegment(mPoint(0, 0), mPoint(2, 2)))
# myFunTest(isIntersectSpan, False, mSpan(0, -1.2), mSpan(1, 2))
# myFunTest(unionSpan, mSpan(1, 9.0), mSpan(1, 3), mSpan(2, 9))
# myFunTest(segIntersectPoint, None, mSegment(mPoint(0, 1), mPoint(0, 2)),
#           mSegment(mPoint(1, 1), mPoint(2, 2)))
# myFunTest(isIntersectSeg, False, mSegment(mPoint(0, 1), mPoint(0, 2)),
#           mSegment(mPoint(1, 1), mPoint(2, 2)))
# myFunTest(isIntersectSeg, True, mSegment(mPoint(0, 0), mPoint(1, 1)),
#           mSegment(mPoint(1, 1), mPoint(3, 3)))
# myFunTest(isIntersectSeg, True, mSegment(mPoint(1, 0), mPoint(1, 1)),
#           mSegment(mPoint(1, 0), mPoint(1, 1)))
# myFunTest(intersectSwall, goal, args)
# myFunTest(unitVector, mVector(1,0),mVector(3,0))
# myFunTest(clwVector, mVector(1, 0), mVector(0, 1))
# myFunTest(reverseVector, mVector(1,1), mVector(-1,-1))
# myFunTest(disclwVector, mVector(-1, 0), mVector(0, 1))
# myFunTest(vectorLength,5, mVector(3,4))
