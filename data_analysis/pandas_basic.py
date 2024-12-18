import pandas as pd

df = pd.read_csv('data_set/netflix_titles.csv')
# print(df.head())
# get the number of rows and columns
# print(df.shape)

# get column names
print(df.columns)

# What is the type of the column names?
# print(df.dtypes)
# get more informatio
# df.info()

titles = df[['title']]
# titles = df['title']
# print(titles)
# print(df.title) # Not recommended as in case of space or special charactre problem arise

# Subset Rows by index Label - .loc[]
# get the first row

# print(df.loc[0])
# Q: How to get last row?
# print(df.loc[-1]) wrong way
#get total row then find last
num_of_rows = df.shape[0]
last_row = df.loc[num_of_rows-1]
# print(last_row)
# get multiple row
# print(df.loc[[1,100,1000]])


# using iloc get second row
# print(df.iloc[1])
# last row using iloc
print(df.iloc[-1])