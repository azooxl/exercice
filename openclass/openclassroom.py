import pandas as pd
import datetime as dt


data = pd.read_csv('operations.csv')
data.head()

data.shape

data.dtypes

data['date_operation'] = pd.to_datetime(data['date_operation'])
data.isnull().sum()
nb_na = data.isnull().sum()
nb_na[nb_na>0]
data.loc[data['montant'].isnull(),:]
data_na = data.loc[data['montant'].isnull(),:]
for index in data_na.index:
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope']
data.loc[data['categ'].isnull(),:]
data.loc[data['libelle'] == 'PRELEVEMENT XX TELEPHONE XX XX', :]
data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'
data.loc[data[['date_operation', 'libelle', 'montant', 'solde_avt_ope']].duplicated(keep=False),:]
data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)
data.describe()
i = data.loc[data['montant']==-15000,:].index[0]
data.iloc[i-1:i+2,:]
data.loc[data['montant']==-15000, 'montant'] = -14.39