
import matplotlib.pyplot as plt
import numpy as np

def feval(funcName, *args):
    return eval(funcName)(*args)

'''
This function/module performs the forward Euler method steps.
'''
def forwardEuler(func, yinit, x_range, h):
    n = int((x_range[-1] - x_range[0])/h) # Number of sub-intervals
    
    x = x_range[0] # Initializes variables x
    y = yinit # Initializes variables y
    
    xsol = np.empty(0) # Creates an empty container for x
    xsol = np.append(xsol, x) # Fills in the first x

    ysol = np.empty(0) # Creates an empty container for y
    ysol = np.append(ysol, y) # Fills in the ICs

    for i in range(n):
        yprime = feval(func, x, y) # Evaluates dy/dx    
        y = y + h*yprime # Eq. (8.2)
        
        x += h # Increases x-step
        xsol = np.append(xsol, x) # Saves it in the container        
        ysol = np.append(ysol, y) # Saves all new y's 
            
    return [xsol, ysol]



def myFunc(x, y):
    '''
    We define our ODEs in this function.
    '''
    dy = (-29*y)
    return dy


h = 0.5
x = np.array([0, 5])
yinit = 1.0


[ts, ys] = forwardEuler('myFunc', yinit, x, h)


# Calculates the exact solution, for comparison
dt = int((x[-1] - x[0]) / h)
t = [x[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = np.exp((-29)*t[i])
    yexact.append(ye)
    
diff = ys - yexact
print("Maximum difference =", np.max(abs(diff)))

plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["Forward Euler method",
            "Exact solution"], loc=1)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()
# Uncomment the following to print the figure:
plt.savefig('Fig_ex2_ForwardEuler.png', dpi=600)

