# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:11:35 2016

@author: winpython
"""
import numpy as np
my_data = np.genfromtxt('data.csv', delimiter = ',')
print ( int(my_data[0][0]) )
print ( my_data[1][0] )
print ( my_data[0][99] )
print ( my_data[99][99] )