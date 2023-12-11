#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:10:36 2023

@author: kennethfraser
"""

import numpy as np

# Values of n you are interested in
n_values = [10, 100, 1000]

# Initialize variables
previous_approximation = None

def true_error(approx_pi, true_value):
    return np.abs(approx_pi - true_value)

def estimated_error(approx_pi, previous_approximation):
    return np.abs(approx_pi - previous_approximation)

true_pi = np.pi

for n in range(1, 1001):
    sum_i = 0
    for i in range(1, n + 1):
        sum_i += 1 / (i**2)
    approx_pi = np.sqrt(6 * sum_i)

    # Check if the current n is in the target_ns
    if n in n_values:
        # True error calculation
        error_true = true_error(approx_pi, true_pi)

        # Estimated error calculation
        if previous_approximation is not None:
            error_estimated = estimated_error(approx_pi, previous_approximation)
        else:
            error_estimated = np.nan

        # Print results
        print('approx_pi')
        print(f"For N = {n}:")
        print(f"Approximation: {approx_pi}")
        print(f"True Error: {error_true}")
        print(f"Estimated Error: {error_estimated}")
        print()