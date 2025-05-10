import pandas as pd

movies_df = pd.read_csv(r'movies.csv')
ratings_df = pd.read_csv('ratings.csv', encoding = "ISO-8859-1")
users_df = pd.read_csv('users.csv', encoding = "ISO-8859-1")

movies_ratings_df = pd.merge(movies_df, ratings_df, on='movieId')
all_df = pd.merge(movies_ratings_df, users_df, on='userId')
all_df.to_csv('combinedData.csv', index=False)

print(all_df.head(10))