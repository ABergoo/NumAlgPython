#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:25:00 2017

@author: August
"""

from scipy import *
from pylab import *
import numpy as np

class Linesearch():
    
    def inexactLinesearch(xk, dk, func, grad): # Notation: see Antoniou Lu pp.112
        """Armijo's rule"""
        epsilon = 0.25
        alpha = 2 
        lamb = 2 # Initial guess for lambda.
        
        def T(x):
            return func(xk) + epsilon*x*grad(xk).T@dk
        
        while func(xk + lamb*dk) > T(lamb) or func(xk + alpha*lamb*dk) < T(alpha*lamb):
            
            if func(xk + lamb*dk) > T(lamb): # The step was too large
                lamb /= alpha
            else: # The step was too small.
                lamb *= alpha
            
        
        return lamb
        
    
    def exactLinesearch(xk, dk, func, grad):
        """The bisection method"""
        a = 0 # Lower interval.
        b0 = 10e99 # Upper interval.
        b = b0
        tol = 0.00001
        itrMax = 100000

        old_lamb = 0
        for i in range(itrMax):
            lamb = (a + b) / 2
            gradNum = grad(xk+lamb*dk)
            
            if (gradNum.T@dk <= 0):
                a = lamb
            else:
                b = lamb
                
            if abs(old_lamb - lamb) < tol:
                break
            old_lamb = lamb
            
        
        return lamb
        
    
    

    
    