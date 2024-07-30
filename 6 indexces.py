import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date

file_1 = pd.read_csv('GZK.csv',
                     index_col=0)
# file_1[:4]
#
# file_1.columns
#
# %timeit file_1[file_1['GZK_DB10.F301']<10]

file_c = file_1.set_index(['GZK_DB10.WIR_601'])
file_c

%timeit file_c[file_c['GZK_DB10.F301']<10]

file_1 = pd.read_csv('GZK.csv')
# float64'
file_cc = file_1.set_index(np.arange(0.0, 505.0, 0.5))

# cathegory index

file_3 = pd.read_csv('GZK.csv')
file_3['name'] = file_3['name'].fillna('other')

file_3['name'] = file_3['name'].astype('category')
# cathegory index list create
cats = file_3['name'].drop_duplicates().tolist()
file_3['name'] = file_3['name'].cat.set_categories(cats)
file_3 = file_3.set_index('name')

# datetimeindex index

file_4 = pd.read_csv('GZK.csv',
                     index_col=0)

file_4.index = pd.to_datetime(file_4.index)

# period index

file_4 = file_4.reset_index()
file_4['DateT'] = file_4['DateTime']
file_4 = file_4.set_index('DateT')
file_4.index = file_4.index.to_period('M')

# index use
file_4.loc['2024-01':'2024-05']

# index use exceptions
file_4.loc[['2024-01', '2024-05', '2024-04']]

# dataset reset index

file_4 = file_4.reset_index()

file_4 = file_4.set_index('DateT')

# index hierarchy
file_4 = file_4.reset_index()

file_4_mult_ind = file_4.set_index(['Index', 'DateTime'])

# index level

len(file_4.index.levels)