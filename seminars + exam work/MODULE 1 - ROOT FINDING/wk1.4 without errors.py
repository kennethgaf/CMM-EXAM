#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:34:46 2023

@author: kennethfraser
"""

import numpy as np

#n is changeable for the value you want
n = 100
sum_i= 0

for i in range(1, n+1):
    sum_i += 1/(i**2)
    approx_pi = np.sqrt(6*sum_i)
print(approx_pi)

