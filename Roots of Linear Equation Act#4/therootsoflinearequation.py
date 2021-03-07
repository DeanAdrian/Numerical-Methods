#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np


# In[36]:


sample1 = lambda x: 2*x**4 + 3*x**3 - 11*x**2 - 9*x + 15
sample2 = lambda x: np.sin(2*x)-np.cos(2*x)
sample3 = lambda x: np.log(x**2+1)
sample4 = lambda x: np.log(x**2-2*x-1)*(x**2-3)


# In[56]:


def regula_falsi(equation, a, b, epochs, precision, n_roots):
    y1, y2 = equation(a), equation(b)
    x_roots = [] 
    epoch = 0
    try:
        if np.allclose(0,y1): x_roots.append(a)
        elif np.allclose(0,y2): x_roots.append(b)
        elif np.sign(y1) == np.sign(y2):
            print("No root here")
        else:
            for epoch in range(epochs):
                c = b - (equation(b)*(b-a))/(equation(b)-equation(a)) ##false root
                if np.allclose(0,equation(c), precision):
                    x_roots.append(c)
                    if len(x_roots) == n_roots:
                        break
                if np.sign(equation(a)) != np.sign(equation(c)): b,y2 = c,equation(c)
                else: a,y1 = c,equation(c) 
    #print("The root is {}, found at {} false position".format(x_roots, epoch))
            if len(x_roots) <= 1:
                print(f"The root is: {x_roots}, found at epoch {epoch}")
            elif len(x_roots) > 1:
                print(f"The roots are: {x_roots}, found at epoch {epoch}")
    except Exception as e:
        print("Error: ", e)
        



# In[64]:


def bisection_method(equation, i1, i2, epochs, precision, n_roots):
    y1, y2 = equation(i1), equation(i2)
    x_roots = []
    end_bisect = 0
    try:
        if np.sign(y1) == np.sign(y2):
            print("Root cannot be found in the given interval")
        else:
            for bisect in range(epochs):
                midp = np.mean([i1,i2])
                y_mid = equation(midp)
                y1 = equation(i1)
                if np.allclose(0, y1, precision):
                  #n_root = i1
                    x_roots.append(i1)
                    end_bisect = bisect
                    if len(x_roots) == n_roots: 
                        break
                if np.sign(y1) != np.sign(y_mid): #root is in first-half interval
                    i2 = midp
                else: #root is in second-half interval
                    i1 = midp 
            if len(x_roots) <= 1:
                print(f"The root is: {x_roots}, found at epoch {end_bisect}")
            elif len(x_roots) > 1:
                print(f"The roots are: {x_roots}, found at epoch {end_bisect}")
    except Exception as e:
        print("Error: ", e)
        



# In[58]:


n_roots = set([]) 

def Secant_Method(equation,n_roots,x0,x1,epochs,Precision):
    print("\nSECANT METHOD")
    ##Checks if Guesses are Equal
    try:
        if equation(x0) == equation(x1):
            print('\nGuesses cannot be Computed\n\n')
        else:
          ##Solves for Root
            for epoch in range(epochs):
                x2 = x0 - equation(x0)*(x1-x0)/( equation(x1) - equation(x0))
                print("Epoch Count: {}, x2 = {}".format(epoch,round(x2,Precision)))
                if np.allclose(x1,x2): 
                    n_roots.add(x2)
                    break
                x0 = x1
                x1 = x2
            print('\nThe root is: {}, found at {} epochs\n'.format(round(x2,Precision),epoch))
            print("The roots found so far are:\n",n_roots)
    except Exception as E:
        print("Error:", E)



