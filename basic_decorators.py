from functools import wraps
import numpy as np

def checkProbs1(fn):
    '''
        It makes sure the summation of prababilites is equal to one, otherwise it raises an error
    '''
    @wraps(fn)
    def wrapper(*args,**kwargs):
        lst = args[0]
        if not (sum(lst ) == 1): raise Exception("Summation of prababilites is not equal to one")
        return fn(*args,**kwargs)
    return wrapper

def checkSize(fn):
    '''
        It makes sure that list size is greater than 2, if 0 raises an error, if 1 return list of zero, if 2 return list of [0,1], otherwise, it calls the function
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        lst = args[0]
        if len(lst) == 0:
            raise Exception("Empty list of probabilites")
        elif len(lst) == 1:
            return np.array([0])
        elif len(lst) == 2:
            return np.array([0,1])
        else:
            return fn(*args,**kwargs)
    return wrapper


def printAnyReturn(fn):
    '''
        if the function returns anything, if prints it. for debug mode.
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result is not None: print(result)
    return wrapper
