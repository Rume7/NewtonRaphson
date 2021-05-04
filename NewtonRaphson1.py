"""
Created on Mon Feb 24 15:37:44 2020
@author: Rhume
"""
# Determine root using Newton-Raphson method

from scipy import misc

def NewtonsMethod(f, x, epsilon=0.000001):
    """ epsilon is the tolerance """
    while True:
        x1 = x - (f(x) / misc.derivative(f, x))
        t = abs(x1 - x)
        if t < epsilon:
            break
        x = x1
    return x

def func1(x):
    return (2.0)*x**2 - (5.0)*x - 1
    
def func2(x):
    return x**3 - 64.0

x = 5

x0 = NewtonsMethod(func2, x)

print('x: ', x)
print('Solution, x0: ', x0)
#print("f(x0) = ", ((1.0/4.0)*x0**3+(3.0/4.0)*x0**2-(3.0/2.0)*x0-2 ))

#eqn = [1, 0, -1, -1]

#print(NewtonsMethod(x0, 1))

