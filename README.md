# pands-project

## Overview ##


This repository was created for the Programming and Scripting module of the ATU Mayo Galway 'Higher Diploma in Computer Programming and Data Analytics' course. It was created to perform a basic exploratory data analysis (EDA) on the Fisher's Iris dataset. The repository contains evidence of the dataset research, Python code, and written documentation, which includes descriptions of the research and the code, as well as references to the materials used during the creation process.

The code conducts a basic exploratory data analysis (EDA) on the Fisher's Iris dataset. It outputs a summary of each variable (i.e., each column in the dataset) to a text file using the **describe()** method of a Pandas DataFrame. Additionally, it saves a histogram of each variable to a PNG file using the **hist()** method of Matplotlib. Furthermore, it generates a scatter plot of each pair of variables using the **scatter()** method of Matplotlib.

Overall, the goal of this code is to provide a basic overview of the dataset and to help identify any patterns or relationships between the variables.

## Fisher's Iris Data Set ##


The Fisher's Iris dataset is widely recognised and commonly used for data analysis and pattern recognition tasks. It was first presented by the British biologist and statistician Ronald Fisher in 1936 in his publication, "The use of multiple measurements in taxonomic problems," as an example of discriminant analysis.

This dataset is a file that contains values separated by commas. The file comprises 150 observations of iris flowers, with four variables measured for each flower: sepal length, sepal width, petal length, and petal width. The observations are equally divided among three species: Iris setosa, Iris versicolor, and Iris virginica. The dataset is often utilised as a beginner's dataset for learning data analysis and machine learning techniques.



## Description of the script ##


The script starts by importing two modules: pandas and matplotlib.pyplot. These modules provide useful functions for working with data and creating visualisations.

Next, it loads a dataset from a CSV file called 'iris.csv' into a special object called 'df'. This dataset contains information about iris flowers.

The script then generates a summary of each variable in the dataset. It does this by using the **describe()** method of the 'df' object, which calculates various statistics such as the count, mean, standard deviation, minimum and maximum values, including the 25th, 50th, and 75th percentiles for the variables. The summary 'df' is transposed using the **transpose()** method to have the variables as rows and statistics as columns. The transposed summary is then converted to a string format using the **to_string()** method.

After that, the script saves this summary to a text file named 'summary.txt'. It writes the string representation of the summary to the file.

Moving on, the script creates histograms for each variable in the dataset. A histogram shows the distribution of values for a particular variable. The **hist()** method from the matplotlib.pyplot module is used to generate these histograms. Each histogram is given a title using the **title()** method and then saved as a PNG file using the **savefig()** method. The **clf()** method is called to clear the current figure, preparing it for the next histogram.

Finally, the script creates scatter plots for each pair of variables in the dataset. A scatter plot displays the relationship between two variables as dots on a graph. The **scatter()** method from the matplotlib.pyplot module is used to create these plots. The **xlabel()** and **ylabel()** methods are used to label the x and y axes, respectively. Each scatter plot is saved as a PNG file using the **savefig()** method, and the **clf()** method is called to clear the current figure for the next scatter plot.

In summary, this script loads and analyses the 'iris.csv' dataset, providing a general summary of the data, creating histograms for each variable, and generating scatter plots to visualise the relationships between variables.



## Research and work on the script for the analysis ##

The in-depth research into Fisher's iris data set was conducted to gain a better understanding of its contents. Extensive research was undertaken, examining various examples of how people analysed this dataset. A wide variety of online resources were consulted to learn how to write a program capable of reading the iris.csv file, analysing the data, providing a general summary, creating histograms for each variable, and generating scatter plots to visualise the relationships between variables.

An analysis.py file was created to work on a script that performs a basic exploratory data analysis on Fisher's Iris dataset and outputs a summary of each variable, saves a histogram of each variable to a PNG file, and generates scatter plots for each pair of variables.

Analysis.py

*#This program performs a basic exploratory data analysis on the Fisher's Iris data set*

*#Outputs a summary of each variable*

*#Saves a histogram of each variable to a PNG file*

*#Outputs a scatter plot of each pair of variables*

*#Author: Tatjana Staunton*



import pandas as pd       *#Importing pandas module*

import matplotlib.pyplot as plt       *#Importing matplotlib.pyplot*


*#Loading the data set from iris.cvs file into pandas DataFrame object df*

df = pd.read_csv('iris.csv') 


*#This part of the code outputs a summary of each variable to a text file*

*#df is used to callculate summary statistics for each column in the data set*

*#This includes the count, mean, standard deviation, minimum and maximum values*

with open('summary.txt', 'w') as f:

f.write(df.describe().to_string())


*#This part of the code saves a histogram of each variable to a png file*

*#It loops over each column in the data frame except the last one*

for column in df.columns[:-1]:

*#Creates a histogram of the data in the column*

plt.hist(df[column])

*#Adds a title to the histogram*

plt.title(column)

*#Saves the histogram to a PNG file with the same name as the column*

plt.savefig(column + '.png')

*#Clears the current figure so we can create a new one*

plt.clf()


*#This part of the code output a scatter plot of each pair of variables*

*It loops over each pair of columns in the data frame except the last one*

for i, column1 in enumerate(df.columns[:-1]):

for j, column2 in enumerate(df.columns[:-1]):

*#Only creates a scatter plot if the pair of columns is different*

if i < j:       *#Creates a scatter plot of the two columns*

plt.scatter(df[column1], df[column2])

*#Adds labels to the x and y axes*

plt.xlabel(column1)

plt.ylabel(column2)

*#Saves the scatter plot to a PNG file with the names of the two columns*

plt.savefig(column1 + '_' + column2 + '.png')

*#Clears the current figure so we can create a new one*

plt.clf()




The code produced the following summary output: 

       5.1         3.5         1.4         0.2

count    149.000000    149.000000    149.000000    149.000000

mean       5.848322      3.051007      3.774497      1.205369

std        0.828594      0.433499      1.759651      0.761292

min        4.300000      2.000000      1.000000      0.100000

25%        5.100000      2.800000      1.600000      0.300000

50%        5.800000      3.000000      4.400000      1.300000

75%        6.400000      3.300000      5.100000      1.800000

max        7.900000      4.400000      6.900000      2.500000
  



The output did not match the desired outcome.
More research  was done to see why it outputs wrong values (one of the most visible things is wrong count). The research suggested to check for missing values.



The program missingvalues.py was created to check for missing values


The code:


import pandas as pd

*#Load the data set*

df = pd.read_csv('iris.csv')

*#Checks for missing values in each column*

missing_values = df.isnull().sum()

with open('summary.txt', 'w') as f:

f.write(df.describe().to_string())


*#Displyes the count of missing values for each variable*

print(missing_values)

The results came back as no missing values.

Correction to the code was made

df = pd.read_csv('iris.csv', na_values=0) 

*#na_values=0 added to 'iris.csv' so pandas will replace any 0 values with NaN in the resulting df for accurate calculations of summary statistics and handling of missing data*





The na_values=0 argument tells pandas that any occurrence of the value 0 in the data should be treated as a missing value (NaN). This way, when reading the CSV file, pandas will replace any 0 values with NaN in the resulting DataFrame, allowing for accurate calculations of summary statistics and handling of missing data



The results of summary did not change.


Then, more corrections were made,


df = pd.read_csv('iris.csv', na_values=0) 

was replaced with

df.replace(0, float('nan'), inplace=True) *Replace 0 values with NaN*


*#Outputs a summary of each variable to a text file*

with open('summary.txt', 'w') as f:

for column in df.columns:

f.write(f"Count for {column}: {df[column].count()}\n")




The results did not change. More research was done to see why the outcome is wrong. It seemed that the program was reading the first row as a heading. Research suggested trying header=None. 


Then, header=None was added to try to stop the program from reading the first row as a heading.



df = pd.read_csv('iris.csv') 

was replaced with

df = pd.read_csv('iris.csv', header=None)



The result of the count in the summary changed from 149 to 150.



Also, an error appeared after the changes.

The error - TypeError: unsupported operand type(s) for +: 'int' and 'str' occurs in the line plt.savefig(column + '.png') 


More research was done to find out why the error was showing up.


The research suggested that the error occurred, because the variable column is of integer type, and the program was trying to concatenate it with a string ('.png').
To fix this error,the column variable was converted to a string before concatenating it with '.png'
By using str(column) instead of just column, the variable is converted to a string, allowing program to concatenate it with '.png' and resolve the error.



Then, the code was further modified to sort the columns in the summary file.


f.write(df.describe().to_string())


was replaced by


summary = df.describe()

summary_transposed = summary.transpose()

f.write(summary_transposed.to_string())


In this modified version, the summary DataFrame is transposed using the transpose() method to have the variables as rows and statistics as columns. Then, the transposed summary is written to the 'summary.txt' file using to_string() method.



The new output:

   count      mean       std  min  25%   50%  75%  max

0  150.0  5.843333  0.828066  4.3  5.1  5.80  6.4  7.9

1  150.0  3.054000  0.433594  2.0  2.8  3.00  3.3  4.4

2  150.0  3.758667  1.764420  1.0  1.6  4.35  5.1  6.9

3  150.0  1.198667  0.763161  0.1  0.3  1.30  1.8  2.5




**Final code** 


import pandas as pd

import matplotlib.pyplot as plt


*#Loads the data set*

df = pd.read_csv('iris.csv', header=None)

df.replace(0, float('nan'), inplace=True) *Replace 0 values with NaN for accurate calculations of summary statistics and handling of missing data*


*#Outputs a summary of each variable to a text file*

with open('summary.txt', 'w') as f:

summary = df.describe()

summary_transposed = summary.transpose()

f.write(summary_transposed.to_string())



*#Saves a histogram of each variable to a png file*

for column in df.columns[:-1]:

plt.hist(df[column])

plt.title(column)

plt.savefig(str(column) + '.png')

plt.clf()


*#Outputs a scatter plot of each pair of variables*

for i, column1 in enumerate(df.columns[:-1]):

for j, column2 in enumerate(df.columns[:-1]):

if i < j:

plt.scatter(df[column1], df[column2])

plt.xlabel(column1)

plt.ylabel(column2)

plt.savefig(str(column1) + '_' + str(column2) + '.png')

plt.clf()




## Referance list ##

https://www.kaggle.com/datasets/vikrishnan/iris-dataset

https://en.wikipedia.org/wiki/Iris_flower_data_set

http://archive.ics.uci.edu/ml/datasets/Iris

https://github.com/gabrielmulligan/fishersirisdataset

https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis

https://salmaneunus27.github.io/Engineer/2021/03/09/blog-1/

https://ourcodingclub.github.io/tutorials/pandas-python-intro/

https://realpython.com/pandas-plot-python/

https://www.edureka.co/community/42836/how-to-read-pandas-csv-file-with-no-header

https://towardsdatascience.com/a-guide-to-pandas-and-matplotlib-for-data-exploration-56fad95f951c

https://www.geeksforgeeks.org/python-data-analysis-using-pandas/

https://www.geeksforgeeks.org/matplotlib-tutorial/

https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python

https://web.microsoftstream.com/video/0ad1b00a-57e5-4deb-9b6f-d549731b55e1

https://www.w3schools.com/python/matplotlib_intro.asp

https://web.microsoftstream.com/video/c244bcfd-c1fa-416c-9ef4-01807c8ef30e

https://web.microsoftstream.com/video/13dfc79c-1203-4e07-8faa-a58e0c5fa030?list=studio

https://www.w3schools.com/python/pandas/default.asp

https://realpython.com/pandas-dataframe/

https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html

https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/index.html

https://web.microsoftstream.com/video/444b5a4a-6133-4120-9db4-e1969fda7d7f

https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

https://www.geeksforgeeks.org/use-of-na_values-parameter-in-read_csv-function-of-pandas-in-python/

https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python#:~:text=Use%20the%20ceil()%20function,and%20print%20the%20resultant%20number.

https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/

https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html

https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-scikit-learn-iris-basic-exercise-1.php

https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
