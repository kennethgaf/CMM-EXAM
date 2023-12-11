#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:23:53 2023

@author: kennethfraser
"""

#the time between initial state (at t=0) and the moment when the sudden
#increase is observed is called the ignition delay.
#compute and report the value of the ignition delay for the 
#three following values of the initial condition:
#-y(0)=0.02
#-y(0)=0.01
#-y(0)=0.005

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

def compute_ignition_delay(t_values, y_values):
    threshold = 0.01 * max(y_values)  # Define a threshold for the sudden increase
    for t, y in zip(t_values, y_values):
        if y > threshold:
            return t

    return None  # Return None if threshold not reached

# Values of the initial condition
initial_conditions = [0.02, 0.01, 0.005]

for y0 in initial_conditions:
    t_result, y_result = euler_method(f, 0, y0, 20, 0.01)
    ignition_delay = compute_ignition_delay(t_result, y_result)

    print(f"For y(0) = {y0}: Ignition Delay = {ignition_delay} seconds")

    plt.plot(t_result, y_result, label=f'y(0)={y0}')

plt.xlabel('t')
plt.ylabel('y')
plt.grid(c = 'lightgrey')
plt.title('Euler Method Solution for dy/dt = 10y^2 - y^3')
plt.axis([0, 22, 0, 11])
plt.legend()
plt.show()

