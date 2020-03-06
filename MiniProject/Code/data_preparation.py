#!/usr/bin/env python3

""" data preparation file for CRat.csv"""
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

# Some imports to explore the datasets
import pandas as pd
#import scipy as sc
#import matplotlib.pylab as pl
#import seaborn as sns # You might need to install this (e.g., sudo pip install seaborn)

# read CRat.csv
data = pd.read_csv("../Data/CRat.csv")

# remove NAs and negative values
data = data[data['N_TraitValue']>=0]
data = data[data['ResDensity']>=0]
data = data[data['ID']>=0]

df = data[['N_TraitValue','ResDensity','ID']]

# write filtered value into new csv file
df.to_csv("../Data/data.csv", encoding='utf-8')