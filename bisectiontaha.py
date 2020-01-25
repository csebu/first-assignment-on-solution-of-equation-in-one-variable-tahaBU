import math

def func(x):
    return 3 * x + math.sin(x) - math.exp(x)

def bisection(a,b):
    while(abs(b-a)>=0):
        m = (a + b) / 2
        if (func(m) == 0.0):
            break
        if(func(a)*func(m))<0:
            b=m
        else:
            a=m
    print("The value of root is : ", "%.8f" % m)
a =0.35
b =0.38
bisection(a, b)