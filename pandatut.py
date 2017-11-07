# Series  one-dimensional array-like object containing an array of data

# Creating Series
import pandas as pd

ds = pd.Series([2, 4, 6, 8, 10])
print(ds)
"""
0     2
1     4
2     6
3     8
4    10
dtype: int64
"""
print(type(ds))
# <class 'pandas.core.series.Series'>

# convert a Panda module Series to Python list and it's type
print(ds.tolist())
print(type(ds.tolist()))
"""
[2L, 4L, 6L, 8L, 10L]
<type 'list'>
"""
#  add, subtract, multiple and divide two Pandas Series.
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)
"""
Divide Series1 by Series2:
0    2.000000
1    1.333333
2    1.200000
3    1.142857
4    1.111111
dtype: float64
"""

# Comparison
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)
"""
Less than:
0    False
1    False
2    False
3    False
4    False
dtype: bool
"""

# DateFrame - Collection of Pandas Series
# From Dictionary
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)
"""
    X   Y   Z                                                          
0  78  84  86                                                          
1  85  94  97                                                          
2  96  89  96                                                          
3  80  83  72                                                          
4  86  86  83 
"""

import numpy as np
# Create and display a DataFrame from a specified dictionary data which has the index labels
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

print("Summary of the basic information about this DataFrame and its data:")
print(df.info())

print("First three rows of the data frame:")
print(df.iloc[:3])

print("Select specific columns:")
print(df[['name', 'score']])

# Select 'name' and 'score' columns in rows 1, 3, 5, 6
print("Select specific columns and rows:")
print(df.ix[[1, 3, 5, 6], ['name', 'score']])

# Select the rows where the score is missing
print("Rows where score is missing:")
print(df[df['score'].isnull()])

# select the rows the score is between 15 and 20 (inclusive).
print("Rows where score between 15 and 20 (inclusive):")
print(df[df['score'].between(15, 20)])

# select the rows where number of attempts in the examination is less than 2 and score greater than 15.
print("Rows where score between 15 and 20 (inclusive):")
print(df[(df['attempts'] < 3) & (df['score'] > 15)])

# change the score in row 'd' to 11.5.
print("\nChange the score in row 'd' to 11.5:")
df.loc['d', 'score'] = 11.5

# sum of the examination attempts by the students
print("\nSum of the examination attempts by the students:")
print(df['attempts'].sum())

print("\nMean score for each different student in data frame:")
print(df['score'].mean())

print("\nAppend a new row:")
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]

print("\nDelete the new row and display the original  rows:")
df = df.drop('k')

print("Sort the data frame first by ‘name’ in descending order, then by ‘score’ in ascending order:")
df.sort_values(by=['name', 'score'], ascending=[False, True])

print("\nReplace the ‘qualify' column contains the values 'yes' and 'no'  with True and  False:")
df['qualify'] = df['qualify'].map({'yes': True, 'no': False})

print("\nChange the name 'James' to ‘Suresh’:")
df['name'] = df['name'].replace('James', 'Suresh')

print("\nDelete the 'attempts' column from the data frame:")
df.pop('attempts')

# insert a new column in existing DataFrame.
print("\nInserting the 'color' column")
color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
df['color'] = color

#  iterate over rows in a DataFrame.
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
df = pd.DataFrame(exam_data)
for index, row in df.iterrows():
    print(row['name'], row['score'])