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

'''
-------------------------------------------------------------------------------
Test
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


def myFunTest(fun, *args, **goal):
    '''report errors if function is failed'''
    import datetime
    if not hasattr(fun, '__call__'):
        error = "1st parameter expect a function/instancemethod(" \
            + type(fun).__name__ + " given)"
        raise TypeError(error)
    startTime = datetime.datetime.now()
    ret = fun(*args)
    endTime = datetime.datetime.now()
    if not (ret == goal['goal']):
        firstLineStr = "Function Error: \"%s\"" % fun.__name__
        l = (79 - len(firstLineStr)) // 2
        line1 = "-" * l + firstLineStr + "-" * l + "\n"
        line2 = "FAIL: " + fun.__name__ +\
            str(args) + " = " + str(ret) +\
            " (type: " + type(ret).__name__ + ")" + "\n"
        line3 = "GOAL: " + str(goal['goal']) + "\n"
        lastLineStr = "Run time: %s" % (endTime - startTime)
        l = (79 - len(lastLineStr)) // 2
        line4 = ("-" * l + lastLineStr + "-" * l)
        raise Warning("\n" + line1 + line2 + line3 + line4)


def myProTest(pro, goal):
    '''report errors if a property is failed'''
    import datetime
    startTime = datetime.datetime.now()
    ret = pro
    endTime = datetime.datetime.now()
    if not (ret == goal):
        raise Warning(
            "\nProperty Error (Run time: %s):\nRESULT: %s\nGOAL: %s" % (
                endTime - startTime, ret, goal))
