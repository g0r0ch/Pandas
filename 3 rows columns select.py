#####
import numpy as np
import pandas as pd

# , index_col='Субъект', # = index column
crm_r = pd.read_csv('CRM.csv', index_col='Субъект', # = index column set
                    sep=';', low_memory=False)
crm_r[:5]
crm_r.columns # = columns name
crm_r.index # = columns name
len(crm_r) # = length DataFrame
crm_r.shape # raws n columns measure
crm_r.size # total symbol amount
crm_r['Unnamed: 2'][:7] # exac column param
crm_r.Субъект # if no spaces else only previous
crm_r[['Unnamed: 1', 'Unnamed: 2']] # few columns output
crm_r.loc[688] # index selection
crm_r.loc['Врач'] # index selection
crm_r.iloc['Врач'] # get position
crm_r.index.getloc[688] # get position
crm_r[:3] # slice first N
crm_r[-3:] # slice last N
crm_r[0:10] # index range
crm_r['ФИО']  <> NaN # bool
crm_r[crm_r['ФИО']  <> NaN]  # flt
crm_r[(crm_r['ФИО']  <> NaN) &
      (crm_r['ФИО']  <> NaN)] # few flt conditions
crm_r[[0:10],
      ['Unnamed:1']]
