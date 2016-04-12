import sys
def get_cur_info():
    print sys._getframe().f_code
    print sys._getframe().f_back.f_code.co_name

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


def a(i):
    '''docstring for a'''

    typeTest([int], i)
    return i

myFunTest(a, 2, 1)
