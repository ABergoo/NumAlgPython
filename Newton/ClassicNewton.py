#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:12:11 2017

@author: Gustav
"""

from scipy import *
from pylab import *

import numpy as np
import scipy.linalg as sl

from GenericNewton import GenericNewton

class ClassicNewton(GenericNewton):
    
    def __init__(self, objGrad, tol):
        super(ClassicNewton, self).__init__(tol)
        self.objGrad = objGrad
        
    
    def step(self, xk):
        delta_x = 0.01
        
        # Create empty Hessian
        H = np.zeros((np.size(xk),np.size(xk)))
        
        # Create a matrix containing rows where only the "current varible x_n is 
        # increased by delta_x (used in finite difference)"
        delta_xk = np.zeros((np.size(xk),np.size(xk)))
        for i in range(np.size(xk)):
            delta_xk[i,i] = delta_x
            
        
        # Calc values of Hessian by finite differences:
        for i in range(np.size(xk)):
            for j in range(np.size(xk)):
                grad1 = self.objGrad(xk + delta_xk[i,:])
                grad2 = self.objGrad(xk)
                H[i, j] = (grad1[j] - grad2[j]) / delta_x
        
        
        # symmetrizing step:
        G = (1/2)*(H + H.transpose())
        
        # Apply choleskys method to turn G into an (upper) trangle matrix.
        A = sl.cholesky(G)
        
        # steplength is calculated through solving a linear eqn sys. with cho_solve():
        # (the zero after A indicates that lower is false i.e. A is an upper)
        steplength = sl.cho_solve((A,0),self.objGrad(xk))
        return steplength
    
    
# Test for potitive definiteness:
def is_pd(K):
    np.linalg.cholesky(K)
    return 1 
