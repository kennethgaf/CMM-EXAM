#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:46:57 2023

@author: kennethfraser
"""

#2017/18 question 2, exact same as 2021 q3

def secant(f, a, b, n):
    if f(a)*f(b) >= 0:
        print('secant method fails, change initial estimation')
        return None, None
    a_n = a
    b_n = b
    for n in range(1, n+1):
        m_n = a_n-f(a_n)*(b-n-a_n)/(f(b_n)-f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print('found exact solution')
            return m_n, n
        else:
            print('secant method fails')
            return None, None
        return a_n-f(a_n)*(b_n-a_n)/(f(b_n)-f(a_n)), n


A = 25500
P = 115000
n = 6    
f = lambda i: ((P*i*(1+i)**n)/(((1+i)**n)-1))-A
solution, iterations = secant(f, 0.01, 1, 100)
sol_round = round(solution, 4)
print('solution as a percentage:', sol_round*100, '%')
print(' no of iters', iterations)