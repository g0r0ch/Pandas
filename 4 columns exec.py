#####
import numpy as np
import pandas as pd

# read csv

crm_r = pd.read_csv('GZK.csv', low_memory=False)
# first columns
# crm_r[:4]
#crm_r.columns
#rename columns via veriable crm_r_1

crm_r_1 = crm_r.rename(columns={'GZK_AI_Out_Cons.AI.Out.Cons1': 'GZK_GZK_GZK',  'GZK_UNS_CNS.AI.Level': 'SMSMSMSM'})
#
# check here is only head transform with no data
crm_r_2 = crm_r.columns[:1].tolist() + crm_r_1.columns[1:].tolist()

#rename columns
crm_r.rename(columns={'GZK_AI_Out_Cons.AI.Out.Cons1': 'GZK_GZK_GZK',  'GZK_UNS_CNS.AI.Level': 'SMSMSMSM'},
             inplace=True)

#add columns
crm_r_c = crm_r.copy()
crm_r_c['total'] = (crm_r_c['GZK_AI_Out_Cons.AI.Out.Cons2']
                             + crm_r_c['GZK_AI_Out_Cons.AI.Out.Cons3']
                             + crm_r_c['GZK_AI_Out_Cons.AI.Out.Cons4'])

#add columns and set place
crm_r_c.insert(39, 'total_2',
               crm_r_c['GZK_DB10.F302']
               + crm_r_c['GZK_DB10.WIR_601']
               )
#refactor column
crm_r_c['total_2'] = crm_r_c['total_2'].round()

#series create with random values
np.random.seed(123456)
s_random = pd.Series(np.random.normal(size=1010),
                     index=crm_r_c.index)

crm_r_c.loc[:, 'sample_col'] = s_random

crm_r_c[:4]


#columns invert

crm_r_c.columns[::-1]

crm_r_c[crm_r_c.columns[::-1]]

#columns delete

# del - удаляет серию из объекта
del crm_r_c['sample_col']

# pop - удаляет и в результате возвращает серию
popped = crm_r_c.pop('total')
#popped
# drop возвращает новый ДФ с удалённым столцом
dropped = crm_r_c.drop(['total_2'],
                       axis=1)
dropped







