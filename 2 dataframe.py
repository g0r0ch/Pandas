#
import numpy as np
import pandas as pd


# DataFrame 1 measure

pd.DataFrame(np.arange(1, 5),
             columns=['num'])

# DataFrame few measures

jp_albums = pd.DataFrame(np.array([[1980, 'British Steel'],
                                  [1981, 'Point of Entry'],
                                  [1982, 'Screaming for Vengeance'],
                                  [1984, 'Defence of the Faith']]),
                        columns=['year', 'album'])

jp_albums

# DataFrame from Series

albums_1 = pd.Series([1986, 'Turbo'])
albums_2 = pd.Series([1988, 'Ram it Down'])
jp_albums_2 = pd.DataFrame([albums_1, albums_2])
jp_albums_2.columns = ['year', 'album']
jp_albums_2

# DataFrame from Series & dict
albums_3_name = pd.Series(['Painkiller', 'Turbo'])
albums_3_year = pd.Series([1980, 1997])
jp_albums_3 = pd.DataFrame({'year': albums_3_year,
                            'album': albums_3_name})
jp_albums_3

# DataFrame fill
albums_4_name = pd.Series(['Demolition', 'Angel of Retribution'])
albums_4_year = pd.Series([2001, 2005])
albums_4_songs = pd.Series([13],
                           index=[1])
jp_albums_4 = pd.DataFrame({'year': albums_4_year,
                            'album': albums_4_name,
                            'nsongs': albums_4_songs})

jp_albums_4
