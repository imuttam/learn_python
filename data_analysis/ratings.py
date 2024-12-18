import pandas as pd


df = pd.read_csv('data_set/netflix_titles.csv')
print(df.columns)
movies = df[df['type'] == 'Movie']

# Sort the DataFrame by the 'rating' column
sorted_movies = movies.sort_values(by='rating', ascending=False)

# Select the 'title' and 'rating' columns
df_ratings = sorted_movies[['title', 'rating']]

# Display the sorted DataFrame
print(df_ratings.head())


