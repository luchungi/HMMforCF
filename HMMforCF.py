# %%
import numpy as np
import pandas as pd
from datetime import datetime
# %%
path = 'D:\\Netflix Dataset\\'
file = 'combined_data_1.txt'
nrows = 100
df = pd.read_csv(path + file, sep=',', header=None, names=['user', 'rating', 'date'], nrows=nrows)
# %%
movie_id_index = pd.DataFrame(pd.isnull(df['rating']))
df_movies = df[df['rating'].isna()]
df_movies = df_movies['user']
df_movies = df_movies.rename('movie_id')
df_movies = df_movies.map(lambda x: x.rstrip(':'))
np_movies = np.stack([df_movies.index.to_numpy(), df_movies.to_numpy()], axis=-1)

# %%
df['movie_id'] = None

for i in range(np_movies.shape[0] - 1):
    # df.iloc[np_movies[i, 0]+1: np_movies[i+1, 0]]['movie_id'] = np_movies[i, 1]
    df.loc[(np_movies[i,0]+1):(np_movies[i+1,0]-1), 'movie_id'] = np_movies[i, 1]
df.loc[(np_movies[-1,0]+1):, 'movie_id'] = np_movies[-1, 1]
df = df.dropna()
# %%

