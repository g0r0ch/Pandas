#####
import numpy as np
import pandas as pd
import datetime


df_1 = pd.read_excel('Ipsos.xlsx',
                     sheet_name='1')

#append

df_2 = pd.read_excel('Ipsos.xlsx',
                     sheet_name='2')

appended = df_1._append(df_2)

#concat

concated = pd.concat([df_1, df_2])

#concat keys

oncated_id_x = pd.concat([df_1, df_2],
                          keys=['south', 'east'])

#add row

concated.loc[100] = ['5556660',
                     'Gleb Kapustin',
                     'SREL-AL']

#delete row

concated = concated.reset_index()
concated.index

#drop
dropped = concated.drop([0, 1])

#flt

more_60 = concated[concated['Pri 1кв`22'] > 60]

#flt sum more then

more_60['Pri 1кв`22'].sum()

#flt slice

slice = concated[-1:]