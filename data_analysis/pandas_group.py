import pandas as pd

df = pd.read_csv('data_set/netflix_titles.csv')

data = df.groupby('type')['release_year'].mean()


ry = df.groupby('release_year')
# for year in ry:
#     if year[0] == 2021:
#         print(year[1]['title'])

country_total = df.groupby('type').sum()
print(country_total['title'].sum())