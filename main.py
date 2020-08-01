# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:20:30 2020
"""
import os
import helper_functions
from scipy.io import loadmat

file = os.path.join(os.getcwd(), 'data_files', 'SalinasA_corrected')
SalinasA_corrected = loadmat(file)

print(SalinasA_corrected.keys())

data  = SalinasA_corrected['salinasA_corrected']

print('The shape of data is ',data.shape)

helper_functions.initialization(data.shape)
