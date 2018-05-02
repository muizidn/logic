from termcolor import colored
from functools import wraps

def printnln(a=''):
    print(a, end='')

def println(a=''):
    print(a)

def crange(a,b):
    return range(a, b+1)

def fib(a):
    if a < 2:
        return a
    else:
        return fib(a-1)+fib(a-2)
    
def pbound(i):
    return i - 1

def pcount(i):
    return i * 2 -1

def total(i):
    return int(i*(i+1)/2)

# Colored Print
def printnlnR(a=''):
    print(colored(a,'red'),end=' ')

def printnlnG(a=''):
    print(colored(a,'green'),end=' ')
    
def printnlnB(a=''):
    print(colored(a,'blue'),end=' ')
    
def doPrint(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
    return wrapper