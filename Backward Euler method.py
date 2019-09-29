import matplotlib.pyplot as plt
import numpy as np

def feval(funcName, *args):
    return eval(funcName)(*args)

'''
This function/module performs the Backward Euler method steps.
'''
def backwardEuler(func, yinit, x_range, h):
    n = int((x_range[-1] - x_range[0])/h)

    x = x_range[0]
    y = yinit

    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        yprime = feval(func, x+h, y)/(1+h)

        y = y+ h*yprime
        x += h
        xsol = np.append(xsol, x)
        ysol = np.append(ysol, y)  # Saves all new y's

    return [xsol, ysol]


def myFunc(x, y):
    '''
    We define our ODEs in this function.
    '''
    dy = (-29*y) 
    return dy


h = 0.5
x = np.array([0, 5])
yinit =1.0


[ts, ys] = backwardEuler('myFunc', yinit, x, h)


# Calculates the exact solution, for comparison
dt = int((x[-1] - x[0]) / h)
t = [x[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = np.exp(-29*t[i])
    yexact.append(ye)

diff = ys - yexact
print("Maximum difference =", np.max(abs(diff)))

plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["Backward Euler method",
            "Exact solution"], loc=2)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()