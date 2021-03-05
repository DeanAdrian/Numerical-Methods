# -*- coding: utf-8 -*-
"""RootsOfLinearEquation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17U-XutaueLosSRy-BKkTWOPfA4zZ4Ofc

# Simple Iterative method
"""

import numpy as np
import matplotlib.pyplot as plt

def iterative_method(equations, n_roots, epochs, precision, x):
  roots = []
  end_epoch = 0
  try:
    for equation in equations:
      x 
      for epoch in range(epochs):
        x_prime = equation(x)
        if np.allclose(x, x_prime, precision):
          if len(roots) == n_roots: break
          roots.append(x)
          break
        x = x_prime
    if len(roots) <= 1:
      print("The root is {} found after {} epochs".format(roots, epoch))
    elif len(roots) > 1:
      print("The roots are {} found after {} epochs".format(roots, epoch))
  except Exception as e:
    print("Error: ", e)

"""# Newton Raphson Method"""

def newton_raphson(equation, equation_prime, epochs, x_inits):
  roots = []
  end_epoch = 0
  for x_init in x_inits:
    x = x_init
    for epoch in range(epochs):
      x_prime = x - (equation(x)/equation_prime(x))
      if np.allclose(x, x_prime):
        ##print(len(roots))
        #if len(roots) == n_roots:  break
        roots.append(x)
        end_epoch = epoch
        break
      x = x_prime
  np_roots = np.round(roots,3)
  np_roots = np.unique(np_roots)
  #print(np_roots)
  if len(roots) <= 1:
    print(f"The root is: {np_roots}, found at epoch {end_epoch+1}")
  elif len(roots) > 1:
    print(f"The roots are: {np_roots}, found at epoch {end_epoch+1}")