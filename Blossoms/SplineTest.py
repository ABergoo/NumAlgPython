# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:04:20 2017
Last updated on 2017-09-07 16.01
@author: Axel, Simon, August
"""
from  scipy import *
from  pylab import *
import numpy as np

import Spline as spl

#Den här filen testar bara vår spline klass. 

# We define boor points and a grid:
bp = np.array([[0,0], [1,1], [2,4], [3,2], [4,7], [5,7], [6,6], [7,5], [8,7], [8,2], [7,2]])
bp2 = np.array([[0,7], [3,3], [1,1], [0,3], [3,4], [6,4], [7,6], [6,7], [5,5], [5,3], [6,1]])
bp3 = np.array([[0,0], [1,4], [5,2], [3,0], [4,4], [5,5], [6,6], [3,9], [1,6], [5,2], [4,4], [3,0], [2,2], [1,1]])
bp4 = np.array([[0.5,.5], [1,0], [1,1], [0,1], [0,0], [1,0], [1,1], [0,1], [0,0], [1,1], [0,0]])

bp5 = np.array([[0,1], [1,2], [3,3], [6,2], [5,3]])
bp6 = np.array([[0,-1],[1,1],[2,-2]])
grid = np.linspace(0, 1, 100)
grid2 = np.linspace(0, 1, 100)

s1 = spl.Spline(bp3, grid)
#s1()
s2 = spl.Spline(bp4, grid2)
#s2()
s3 = spl.Spline(bp5, grid2)
#s3()
s4 = spl.Spline(bp, grid2)
#s4()

s_comb= s2 + s1 + s3
s_comb()
