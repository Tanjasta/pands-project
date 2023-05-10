import pandas as pd

# Load the data set
df = pd.read_csv('iris.csv')

# Check for missing values in each column
missing_values = df.isnull().sum()

# Display the count of missing values for each variable
print(missing_values)
