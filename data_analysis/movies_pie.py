import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_set/netflix_titles.csv')

# print(df['type'])
# print(df['type'].nunique())
coulmns = df.columns
print(coulmns)

movies = df[df['type'] == 'Movie']
movies_count = movies.type.count()
# print(f'Total Movies listed: {movies_count}')


tv_series = df[df['type'] == 'TV Show']
tv_count = tv_series.type.count()
# print(f'Tptal TV Shows listed: {tv_count}')

data = [movies_count, tv_count]
labels = ['Movies', 'TV']

# plt.pie(data,labels=labels, textprops={"color":'black'}, autopct='%0.2f')
# plt.title("Movies verses TV in %")

# plt.show()

indian_movies = df[(df['type'] == 'Movie') & (df['country'] == 'India')]
indian_movies_count = indian_movies.type.count()
print(indian_movies_count)
rest_movies = movies_count-indian_movies_count
print(f"Total Indian Movies: {indian_movies_count}")

data_indian = [indian_movies_count, rest_movies]


plt.pie(data_indian,labels=['Indian', 'Rest of World'], textprops={"color":'black'}, autopct='%0.2f', explode=(0,0.1))
plt.title("Indian Movies verses Rest in %")
plt.show()

