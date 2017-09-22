#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:34:54 2017

@author: Simon
"""

from scipy import *
from pylab import *

from OptimizationProblem import OptimizationProblem
import numpy as np

# func = x^2 + x + 1
# grad = 2x + 1
# x0 = np.array(0, 1)
# tol = 1e-6
# Methods = 'ClassicNewton', 'GoodBroyden', 'BadBroyden', 'DFP' and 'BFGS'
# Linesearch = 'Inexact' and 'Exact'

# problem1.solve(x0, tol, 'BadBroyden', 'Exact')

def f(x):
    return np.array(x**3)

def grad(x):
    return np.array(3*x**2)

problem1 = OptimizationProblem(f, grad)
tol = 1e-5
x0 = np.array([0.01])
problem1.solve(x0, tol, 'ClassicNewton')



