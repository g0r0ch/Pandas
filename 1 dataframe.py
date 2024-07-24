# Pandas
import pandas as pd
import numpy as np
#  lists dataframe columns
name = ['Rocka Rolla', 'Sad Wings of Destiny', 'Sin after sin', 'Stained class', 'Killing machine']
year = [1974, 1976, 1977, 1978, 1978]

#  dict
albums_dict = {'album': name,
               'realise_year': year}
# albums_dict

#  DataFrame
albums_df = pd.DataFrame(albums_dict)
# albums_df.index
albums_df.index = ['a', 'b', 'c', 'd', 'e']
albums_df.index

albums_df_2 = pd.DataFrame([{'album': 'Point of Entry',
                            'year': 1981},
                            {'album': 'Screaming for Vengeance',
                            'year': 1982}],
                           columns=['year', 'album'])
albums_df_2

# CSV

albums_df.to_csv('jp_albums.csv',
                 index=False)
