#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:05:38 2023

@author: kennethfraser
"""

import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return 10 * y**2 - y**3

def euler_method(f, t0, y0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = [y0]

    for t in t_values[:-1]:
        y_next = y_values[-1] + h * f(t, y_values[-1])
        y_values.append(y_next)

    return t_values, y_values

t0 = 0
y0 = 0.02
t_values = [4, 5, 10]
h = 0.01

t_result, y_result = euler_method(f, t0, y0, max(t_values), h)

for t in t_values:
    index = int(t / h)
    y_at_t = y_result[index]
    print(f"At t={t}: y={y_at_t}")

plt.plot(t_result, y_result, label='Euler Method', c = 'magenta')
plt.grid(c = 'lightgrey')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler Method Solution for dy/dt = 10y^2 - y^3')
plt.axis([0, 10, 0, 12])
plt.legend()
plt.show()
