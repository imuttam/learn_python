import pandas as pd

df = pd.read_csv('data_set/netflix_titles.csv')

# subset columns with loc
# note the position of the colon
# it is used to select all rows
subset = df.loc[:, ['title', 'country']]
# print(subset)

# subset columns with iloc
# iloc will allow us to use integers
# -1 will select the last column
subset1 = df.iloc[:, [2, 1, -2]]
# print(subset1)

# We will get an error if we don’t specify .loc[] or iloc[] correctly.

# using range
r = list(range(6))
subset2 = df.iloc[:, r]
# print(subset2)

# what is movie title in first row

subset3 = df.loc[0, 'title']
# print(subset3)

# same using iloc
subset4 = df.iloc[0, 2]
# print(subset4)

# get the 1st, 100th, and 1000th rows
# from the 2st, 8th, and 9th column
# note the columns we are hoping to

subset5 = df.iloc[[1,100,1000], [2,8,9]]
print(subset5)

# using loc
# get the 1st, 100th, and 1000th rows
# from the 2st, 8th, and 9th column
# note the columns we are hoping to
# More readable
subset6 = df.loc[[1,100,1000], ['title','country','rating']]
print(subset6)