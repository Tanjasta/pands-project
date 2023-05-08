# Analysis.py
# This program performs a basic exploratory data analysis (EDA) on the Fisher's Iris data set.
# Outputs a summary of each variable 
# Saves a histogram of each variable to a PNG file
# Outputs a scatter plot of each pair of variables
# Author: Tatjana Staunton

import pandas as pd # Importing pandas module
import matplotlib.pyplot as plt # Importing matplotlib.pyplot

df = pd.read_csv('iris.csv') # Loading the data set from iris.cvs file into pandas DataFrame object df
