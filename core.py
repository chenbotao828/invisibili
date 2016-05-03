# coding=utf-8
'''
-------------------------------------------------------------------------------
Const data of invisibili
-------------------------------------------------------------------------------
'''


class myObject(object):
    "My Object "

    def __init__(self):
        pass

    def __eq__(self, another):
        # sd == ad:
        if type(self) == type(another) and self.__dict__ == another.__dict__:
            return True
        return False

    def __hash__(self):
        return hash((type(self), self.args))

    @property
    def args(self):
        '''args for model'''

        ret = []
        for p in self.para:
            if p[0:2] == "**":
                raise Exception("\"**\" parameter is not allowed")
            if p[0] == "*":
                ret += self.__dict__[p.lstrip("*")]
            else:
                ret.append(self.__dict__[p])
        return tuple(ret)

    def __repr__(self):
        if type(self.args) != tuple:
            return type(self).__name__ + "(" + str(self.args) + ")"
        return type(self).__name__ + str(self.args)

    def move(self, v):
        '''move along vector'''

        typeTest([vector], v)
        ret = self
        for apara in self.para:
            if isinstance(self.__dict__[apara], point):
                ret.__dict__[apara] = self.__dict__[apara].move(v)
        return ret

    @property
    def sympy_name(self):
        '''return model's sympy model name if exist (str)'''

        ret = self.__class__.__name__.title()
        try:
            eval(ret)
        except:
            raise TypeError("%s don't have sympy_name" %
                            self.__class__.__name__)
        return ret

    @property
    def sympy(self):
        '''return sympy object'''

        return eval(self.sympy_name + str(self.args).title())

    def copy(self):
        '''return shallow copy'''

        return eval(self.__class__.__name__ + str(tuple(self.args)))

    def set_attr(self, **new):
        '''return model of new attributes'''

        new_args = list(self.args)
        for key in new:
            new_args[self.para.index(key)] = new[key]
        return eval(fun(self.__class__, new_args))

    # def intersection(self, another):
    #     '''return intersection list'''

    #     typeTest([myObject], another)
    #     try:
    #         A = eval(self.sympy_name + str(self.args).title())
    #         B = eval(another.sympy_name + str(another.args).title())
    #         return map(lambda x: eval(x.__repr__().lower()), A.intersection(B))
    #     except:
    #         raise TypeError("Can not intersect")


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
        # if type(typeList[i]) in [list, tuple]:
        if isinstance(typeList[i], (list, tuple)):
            # if type(args[i]) not in typeList[i]:
            if not isinstance(args[i], tuple(typeList[i])):
                raise TypeError("%dth parameter expect %s, given %s \"%s\"" %
                                (i + 1, str([x.__name__ for x in typeList[i]]),
                                 type(args[i]).__name__, str(args[i])))
        # elif type(args[i]) != typeList[i]:
        elif not isinstance(args[i], typeList[i]):
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


def fun(fun, args):
    '''return str of a function/type/instancemethod with iterable sequence as args'''

    if not hasattr(fun, '__call__'):
        error = "1st parameter expect a function/type/instancemethod(" \
            + type(fun).__name__ + " given)"
        raise TypeError(error)
    try:
        argsTuple = tuple(args)
    except:
        argsTuple = (args,)
    return fun.__name__ + str(argsTuple)


def sympy2m(sympy_model):
    '''sympy object to myObject str'''

    return sympy_model.__repr__().lower()


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated
    function recurses in a non-tail context.
    """
    def func(*args, **kwargs):
        import sys
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
                and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
'''
@tail_call_optimized
def factorial(n, acc=1):
  "calculate a factorial"
  if n == 0:
    return acc
  return factorial(n-1, n*acc)

print factorial(10000)
'''
