#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:34:11 2023

@author: kennethfraser
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def f(x):
    return (2*np.sin(x))-((x**2)/10)

x_values = np.linspace(0, 10, 100)
y_values = f(x_values)

max_y = max(y_values)
max_x = x_values[y_values.argmax()]

x_val = round(max_x, 3)
y_val = round(max_y, 3)

plt.figure()
plt.plot(x_values, y_values, c = 'blue')
plt.grid()
plt.ylim(-10, 4)
plt.xlim(0, 10)
plt.text(2, 2, str((x_val, y_val)), c = 'blue')
print(x_val, y_val)
plt.show()