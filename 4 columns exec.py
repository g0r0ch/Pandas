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
               crm_r_c['GZK_AI_Out_Cons.AI.Out.Cons2']
               + crm_r_c['GZK_AI_Out_Cons.AI.Out.Cons3']
               )
#refactor column
crm_r_c['total_1'] = crm_r_c['total_1'].round()













