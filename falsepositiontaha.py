import math


def func(x):
    return 3 * x + math.sin(x) - math.exp(x)

def false(a,b):
    while(abs(b-a)>0):
       if (func(a)*func(b)<0):
           m=((a*func(b))-(b*func(a)))/(func(b)-func(a))
       if (func(m) == 0.0):
           break
       elif (func(a) * func(m)) < 0:
           b = m
       else:
           a = m
    print("The value of root is : ", "%.8f" % m)
a=0
b=1
false(a,b)
