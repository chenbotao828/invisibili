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


class myObject(object):
    "my modified Object"

    def __init__(self, *args):
        pass

    def __str__(self):
        return type(self).__name__ + str(self.args)

    def __eq__(self, anonther):
        if self.args == anonther.args and type(self) == type(anonther):
            return True
        return False


class myVector(myObject):
    "my simple 2D vector, tuple of 2 num"

    def __init__(self, i, j):
        typeTest([(int, float, long)] * 2, i, j)
        self.i = i
        self.j = j
        self.args = (i, j)


class myPoint(myObject):
    '''my simple 2D point'''

    def __init__(self, x, y):

        typeTest([const.typeNum] * 2, x, y)
        self.args = (x, y)
        self.x = x
        self.y = y


class mySwall(myObject):
    '''my simple straight wall'''

    def __init__(self, start, end, lw=100, rw=100, attDict={}):

        typeTest([myPoint, myPoint, const.typeNum, const.typeNum, dict],
                 start, end, lw, rw, attDict)
        self.args = (start, end, lw, rw, attDict)
        self.start = start
        self.end = end
        self.lw = lw
        self.rw = rw
        self.attDict = attDict


class mySegment(myObject):
    '''my simple 2d segment'''

    def __init__(self, p1, p2):

        typeTest([myPoint, myPoint], p1, p2)
        self.args = (p1, p2)
        self.p1 = p1
        self.p2 = p2


class linearEquation(myObject):
    "y = ax + b for x in [xMin, xMax]"

    def __init__(self, a, b, xMin, xMax):

        typeTest([const.typeNum] * 4, a, b, xMin, xMax)
        self.args = (a, b, xMin, xMax)
        self.a = a
        self.b = b
        self.xMin = xMin
        self.xMax = xMax


class vtclinearEquation(myObject):
    '''x = c for y in[yMin, yMax]'''

    def __init__(self, c, yMin, yMax):

        typeTest([const.typeNum] * 3, c, yMin, yMax)
        self.args = (c, yMin, yMax)
        self.c = c
        self.yMin = yMin
        self.yMax = yMax


class mySpan(myObject):
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
    "Type test of args inside a function or a class"
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
    "report errors if function is failed"
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
        print "-" * l + firstLineStr + "-" * l
        print("FAIL: " + fun.__name__ +
              str(args) + " = " + str(ret)) +\
            " (type: " + type(ret).__name__ + ")"
        print("GOAL: " + str(goal))
        lastLineStr = "Run time: %s" % (endTime - startTime)
        l = (79 - len(lastLineStr)) // 2
        print "-" * l + lastLineStr + "-" * l


def isNum(value):
    "return True if value is int, float ..."
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True


def vectorLength(aVector):
    "return length of a vector"
    typeTest([myVector], aVector)
    return (aVector.i**2 + aVector.j**2)**0.5


def unitVector(aVector):
    "return unit vector, (0,0) returns itself"
    typeTest([myVector], aVector)
    if aVector == myVector(0, 0):
        return aVector
    else:
        l = vectorLength(aVector)
        i = aVector.i / l
        j = aVector.j / l
        return myVector(i, j)


def clwVector(aVector):
    '''return 90 degree clockwise of the vector'''

    typeTest([myVector], aVector)
    return myVector(aVector.j, -aVector.i)


def reverseVector(aVector):
    '''return a reversed vector'''

    typeTest([myVector], aVector)
    return myVector(-aVector.i, -aVector.j)


def disclwVector(aVector):
    '''return 90 degree disclockwise vector'''

    typeTest([myVector], aVector)
    return reverseVector(clwVector(aVector))


def segEquation(aSeg):
    '''return linear equation object of a segment'''

    typeTest([mySegment], aSeg)
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

    typeTest([mySegment], aSeg)
    if type(segEquation(aSeg)) == vtclinearEquation:
        return float("inf")
    else:
        return segEquation(aSeg).a

# myFunTest(segSlope, 1, mySegment(myPoint(0, 0), myPoint(2, 2)))


def isIntersectSpan(span1, span2):
    '''return True if a span intersect another'''

    typeTest([mySpan] * 2, span1, span2)
    if span1.b < span2.a or span2.b < span1.a:
        return False
    return True

# myFunTest(isIntersectSpan, False, mySpan(0, -1.2), mySpan(1, 2))


def numInSpan(num, aSpan):
    '''return True if a num is in a range '''

    typeTest([const.typeNum, mySpan], num, aSpan)
    if aSpan.a <= num <= aSpan.b:
        return True
    return False


# myFunTest(numInSpan, False, -1, mySpan(0, 2))


def isIntersectSeg(seg1, seg2):
    '''return True if a segment intersect anonther'''

    typeTest([mySegment] * 2, seg1, seg2)
    if segSlope(seg1) == segSlope(seg2) == float("inf"):
        c1, yMin1, yMax1 = segEquation(seg1).args
        c2, yMin2, yMax2 = segEquation(seg2).args
        if c1 == c2 and isIntersectSpan(
                mySpan(yMin1, yMax1), mySpan(yMin2, yMax2)):
            return True
        else:
            return False
    elif float("inf") in map(segSlope, [seg1, seg2]):
        if segSlope(seg1) == float("inf"):
            seg1, seg2 = seg2, seg1
        a, b, xMin, xMax = segEquation(seg1).args
        c, yMin, yMax = segEquation(seg2).args
        y = a * c + b
        if numInSpan(y, mySpan(yMin, yMax)) and \
                numInSpan(c, mySpan(xMin, xMax)):
            return True
        return False
    else:
        a1, b1, xMin1, xMax1 = segEquation(seg1).args
        a2, b2, xMin2, xMax2 = segEquation(seg2).args
        if a1 == a2:
            if b1 == b2 and isIntersectSpan(
                    mySpan(xMin1, xMax1), mySpan(xMin2, xMax2)):
                return True
            return False
        else:
            x = (b2 - b1) / (a1 - a2)
            if numInSpan(x, mySpan(xMin1, xMax1)) and \
                    numInSpan(x, mySpan(xMin2, xMax2)):
                return True
            return False


def segIntersectPoint(seg1, seg2):
    '''return intection Point of two segment'''

    typeTest([mySegment] * 2, seg1, seg2)
    if not isIntersectSeg(seg1, seg2):
        return None
    else:
        if segSlope(seg1) == segSlope(seg2) == float("inf"):
            pass

# myFunTest(segIntersectPoint, None, mySegment(myPoint(0, 1), myPoint(0, 2)),
#           mySegment(myPoint(1, 1), myPoint(2, 2)))
myFunTest(isIntersectSeg, False, mySegment(myPoint(0, 1), myPoint(0, 2)),
          mySegment(myPoint(1, 1), myPoint(2, 2)))
# myFunTest(isIntersectSeg, True, mySegment(myPoint(0, 0), myPoint(1, 1)),
#           mySegment(myPoint(1, 1), myPoint(3, 3)))
# myFunTest(isIntersectSeg, True, mySegment(myPoint(1, 0), myPoint(1, 1)),
#           mySegment(myPoint(1, 0), myPoint(1, 1)))


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

# myFunTest(intersectSwall, goal, args)
# myFunTest(unitVector, myVector(1,0),myVector(3,0))
# myFunTest(clwVector, myVector(1, 0), myVector(0, 1))
# myFunTest(reverseVector, myVector(1,1), myVector(-1,-1))
# myFunTest(disclwVector, myVector(-1, 0), myVector(0, 1))
# myFunTest(vectorLength,5, myVector(3,4))
