# Analysis.py
# This program performs a basic exploratory data analysis (EDA) on the Fisher's Iris data set.
# Outputs a summary of each variable 
# Saves a histogram of each variable to a PNG file
# Outputs a scatter plot of each pair of variables
# Author: Tatjana Staunton

import pandas as pd # Importing pandas module
import matplotlib.pyplot as plt # Importing matplotlib.pyplot

df = pd.read_csv('iris.csv', na_values=0) # Loading the data set from iris.cvs file into pandas DataFrame object df
# na_values=0 added to 'iris.csv' so pandas will replace any 0 values with NaN in the resulting df 
# for accurate calculations of summary statistics and handling of missing data

# This part of the code outputs a summary of each variable to a text file
# df is used to callculate summary statistics for each column in the data set
# This includes the count, mean, standard deviation, minimum and maximum values (incl. 25th/50th/75th percentiles) .
with open('summary.txt', 'w') as f:
    f.write(df.describe().to_string())

# This patr of the code saves a histogram of each variable to a png file
# It loops over each column in the data frame except the last one (which contains the target variable)
for column in df.columns[:-1]:
    # Creates a histogram of the data in the column
    plt.hist(df[column])
    # Adds a title to the histogram
    plt.title(column)
    # Saves the histogram to a PNG file with the same name as the column
    plt.savefig(column + '.png')
    # Clears the current figure so we can create a new one
    plt.clf()

# This part of the code output a scatter plot of each pair of variables
# It loops over each pair of columns in the data frame except the last one
for i, column1 in enumerate(df.columns[:-1]):
    for j, column2 in enumerate(df.columns[:-1]):
        # Only creates a scatter plot if the pair of columns is different
        if i < j:
            # Creates a scatter plot of the two columns
            plt.scatter(df[column1], df[column2])
            # Adds labels to the x and y axes
            plt.xlabel(column1)
            plt.ylabel(column2)
            # Saves the scatter plot to a PNG file with the names of the two columns
            plt.savefig(column1 + '_' + column2 + '.png')
            # Clears the current figure so we can create a new one
            plt.clf()

# Perform other analysis of the choice as appropriate

