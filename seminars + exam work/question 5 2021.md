#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:19:27 2023

@author: kennethfraser
"""

flowrate for a cylinder: Q = A*sqrt(2gh)
flowrate for the basin: Q = A*sqrt(integral of (b+sz)**hdz with limits h,0)
Volume for a cylinder = pi*r**2*h
volume for a basin = pi*(integral of ((b+sz)**2dz) with limits h,0)

Time to drain = V/Q

2T_cylinder = T_basin as doubles:

2pi*r**2*h/A*sqrt(2gh) =  
