import matplotlib.pyplot as plt
import numpy as np


'''
This function/module performs the Runge-Kutta method method steps.
'''
def RK4thOrder(func, yinit, x_range, h):
    n = int((x_range[-1] - x_range[0])/h)
    
    x = x_range[0]
    y = yinit
    
    # Containers for solutions
    xsol = np.empty(0)
    ysol = np.empty(0)

    xsol = np.append(xsol, x)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)
        yp2 = y + k1*(h/2)
        k2 = feval(func, x+h/2, yp2)
        yp3 = y + k2*(h/2)
        k3 = feval(func, x+h/2, yp3)
        yp4 = y + k3*h
        k4 = feval(func, x+h, yp4)

        y = y + (h/6)*(k1 + 2*k2 + 2*k3+ k4)

        x = x + h
        xsol = np.append(xsol, x)

        ysol = np.append(ysol, y)  

    return [xsol, ysol]


def feval(funcName, *args):
    return eval(funcName)(*args)

def myFunc(x, y):
    dy = (-29*y) 
    return dy

h = 0.5
x = np.array([0, 5])
yinit = 1.0

[ts, ys] = RK4thOrder('myFunc', yinit, x, h)


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
plt.legend(["4th Order RK", "Exact solution"], loc=1)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()

# Uncomment the following to print the figure:
plt.savefig('Fig_ex2_RK4_h0p1.png', dpi=600)

