# pands-project

## Overview##
This repository was created for the Programming and Scripting module of the ATU Mayo Galway 'Higher Diploma in Computer Programming and Data Analytics' course. It was created to perform a basic exploratory data analysis (EDA) on the Fisher's Iris dataset. The repository contains evidence of the dataset research, Python code, and written documentation, which includes descriptions of the research and the code, as well as references to the materials used during the creation process. The code conducts a basic exploratory data analysis (EDA) on the Fisher's Iris dataset.
It outputs a summary of each variable (i.e., each column in the dataset) to a text file using the **describe()** method of a Pandas DataFrame. Additionally, it saves a histogram of each variable to a PNG file using the **hist()** method of Matplotlib. Furthermore, it generates a scatter plot of each pair of variables using the **scatter()** method of Matplotlib.
Overall, the goal of this code is to provide a basic overview of the dataset and to help identify any patterns or relationships between the variables.


## Fisher's Iris Data Set ##
The Fisher's Iris dataset is a is a widely recognised dataset that is commonly used for data analysis and pattern recognition tasks. It was first presented by the British biologist and statistician Ronald Fisher in 1936 in his publication, "The use of multiple measurements in taxonomic problems," as an example of discriminant analysis.
This dataset is a file that has values separated by commas. The file consists of 150 observations of iris flowers, with four variables measured for each flower: sepal length, sepal width, petal
length, and petal width. The observations are divided equally among three
species: Iris setosa, Iris versicolor, and Iris virginica. The dataset is often
used as a beginner's dataset for learning data analysis and machine learning
techniques.



## Description of the script ##


The script starts by importing two modules: pandas and matplotlib.pyplot. These modules provide useful functions for working with data and creating visualizations.
Next, it loads a dataset from a CSV file called **'iris.csv'** into a special object called 'df'. This dataset contains information about flowers.
The script then generates a summary of each variable in the dataset. It does this by using the **describe()** method of the 'df' object, which calculates various statistics such as the count, mean, standard deviation, minimum and maximum values including 25th/50th/75th percentiles for the variables. The summary 'df' is transposed using the **transpose()** method to have the variables as rows and statistics as columns. The transposed summary is then converted to a string format using the **to_string()** method.
After that, the script saves this summary to a text file named **'summary.txt'**. It writes the string representation of the summary to the file.
Moving on, the script creates histograms for each variable in the dataset. A histogram shows the distribution of values for a particular variable. The **hist()** method from the matplotlib.pyplot module is used to generate these histograms. Each histogram is given a title using the **title()** method, and then saved as a PNG file using the **savefig()** method. The **clf()** method is called to clear the current figure, preparing it for the next histogram.
Finally, the script creates scatter plots for each pair of variables in the dataset. A scatter plot displays the relationship between two variables as dots on a graph. The **scatter()** method from the matplotlib.pyplot module is used to create these plots. The **xlabel()** and **ylabel()** methods are used to label the x and y axes respectively. Each scatter plot is saved as a PNG file using the **savefig()** method, and the **clf()** method is called to clear the current figure for the next scatter plot.
In summary, this script loads and analyses the 'iris.csv' dataset, providing a general summary of the data, creating histograms for each variable, and generating scatter plots to visualize the relationships between variables.



## Reasearch and work on the script for analysis ##


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

https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/

https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html

https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-scikit-learn-iris-basic-exercise-1.php

https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
