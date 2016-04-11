# coding=utf-8
'''
Functions of invisibili
'''

"const:"
_typeNum = [int, float, long]


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


def isNum(value):
    "return True if value is int, float ..."
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True


class myVector(myObject):
    "my simple 2D vector, tuple of 2 num"

    def __init__(self, i, j):
        typeTest([(int, float, long)] * 2, i, j)
        self.i = i
        self.j = j
        self.args = (i, j)


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


class myPoint(myObject):
    '''my simple 2D point'''

    def __init__(self, x, y):

        typeTest([_typeNum, _typeNum], x, y)
        self.args = (x, y)
        self.x = x
        self.y = y


class swall(myObject):
    '''my simple straight wall'''

    def __init__(self, start, end, lw=100, rw=100, attDict={}):

        typeTest([myPoint, myPoint, _typeNum, _typeNum, dict],
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
    '''y = ax + b for x in [xMin, xMax]'''

    def __init__(self, a, b, xMin, xMax):

        typeTest([_typeNum]*4, a, b, xMix, xMax)
        self.args = (a, b, xMax)
        self.a = a
        self.b = b
        self.xMin = xMin
        self.xMax = xMax


def isIntersect(s1, s2):
    '''return True if s1 intersect s2'''

    typeTest([mySegment, mySegment], s1, s2)
    if

myFunTest(isIntersect, False,
          mySegment(myPoint(0, 0),
                    myPoint(1, 0)),
          mySegment(myPoint(0, 0),
                    myPoint(0, 1)))


def intersectSwall(s1, s2):
    '''return intersection of two Swalls, swall list'''

    typeTest([swall, swall], s1, s2)
    if isIntersect((s1.start, s1.end), (s2.start, s2.end)):
        ip = intersectionPoint((s1.start, s1.end), (s2.start, s2.end))

# myFunTest(intersectSwall, goal, args)
# myFunTest(unitVector, myVector(1,0),myVector(3,0))
# myFunTest(clwVector, myVector(1, 0), myVector(0, 1))
# myFunTest(reverseVector, myVector(1,1), myVector(-1,-1))
# myFunTest(disclwVector, myVector(-1, 0), myVector(0, 1))
# myFunTest(vectorLength,5, myVector(3,4))
