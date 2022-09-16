#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# 
# This script plots a fractal geometry and generates a maximization of 
# an specific section of the figure.
#
# 2019 David Quezada, Krakow, Poland
# email [dqreator@gmail.com]
# -----------------------------------------------------------
import random
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')
plt.rcParams['font.size'] = 20


def new_point(x_last, y_last):
    """Function that generates a new point following the fractal geometry.
    Args:
        x_last (float): Last value x
        y_last (float): Last value y
    """
    # Generate a new uniform number from 0-1
    p = random.uniform(0, 1)
    # Determine the new coordinates of the point 
    if (p <= 0.85):
        x_new = 0.85*x_last+0.04*y_last
        y_new = -0.04*x_last+0.85*y_last+1.6
    elif(p > 0.85) and (p <= 0.92):
        x_new = 0.2*x_last-0.26*y_last
        y_new = 0.23*x_last+0.22*y_last+1.6
    elif(p > 0.92) and (p <= 0.99):
        x_new = -0.15*x_last+0.28*y_last
        y_new = 0.26*x_last+0.24*y_last+0.44
    else:
        x_new = 0
        y_new = 0.16*y_last
    return[x_new, y_new]


# Number of points
number_points = 10**5

# Initialize variables
X = [0]                 
Y = [0]
X_MAX = [0]               
Y_MAX = [0]
x0 = 0
y0 = 0

for i in range(0, number_points-1):
    [x, y] = new_point(x0, y0)
    X.append(x)
    Y.append(y)
    x0 = x
    y0 = y

X = np.array(X)
Y = np.array(Y)

while len(X_MAX) < number_points:
    [x, y] = new_point(x0, y0)
    if (x >= -1) and (x <= 0) and (y >= 2) and (y <= 3.5):
        X_MAX.append(x)
        Y_MAX.append(y)
    x0 = x
    y0 = y
    
X_MAX = np.array(X_MAX)
Y_MAX = np.array(Y_MAX)

# Define the first plot 
plt.subplot(1, 2, 1)
plt.plot(X, Y, 'b,')

# Define red square 
plt.plot([-1, 0], [2, 2], 'r-', lw=5)
plt.plot([-1, 0], [3.5, 3.5], 'r-', lw=5)
plt.plot([-1, -1], [2, 3.5], 'r-', lw=5)
plt.plot([0, 0], [2, 3.5], 'r-', lw=5)

# Define the second plot 
plt.subplot(1, 2, 2)
plt.plot(X_MAX, Y_MAX, 'b,')

# Define red square 
plt.plot([-1, 0], [2, 2], 'r-', lw=5)
plt.plot([-1, 0], [3.5, 3.5], 'r-', lw=5)
plt.plot([-1, -1], [2, 3.5], 'r-', lw=5)
plt.plot([0, 0], [2, 3.5], 'r-', lw=5)


# Show plots
plt.show()