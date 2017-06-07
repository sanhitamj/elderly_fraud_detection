'''

Reads in an SQL table IncomeExpenseTransactions from the database called
ConservatorDatabase as a Pandas dataframe.

Removes some columns and some rows

Modifies some columns, feature engineering begins

Writes out a csv file called expense.csv

'''


from sqlalchemy import create_engine
import pandas as pd
from pandas.io import sql
import numpy as np
import datetime

def establish_conection(password, databasename = 'ConservatorDatabase', username = 'sa', hostname = 'localhost', port = '1433') :
    '''
    Establishes sqlalchemy connection to a mssql database

    Need to give it a password; default user = sa, port = 1433, hostname = localhost, databasename = ConservatorDatabase
    username, password, hostname, port, databasename

    returns engine
    '''
    engine_string = 'mssql+pymssql://' + username + ':' + password + '@' + hostname + ':' + port + '/' + databasename

    return create_engine(engine_string)

def read_sql_table(tablename):
    '''
    tablename as a string
    read table in pandas, return query as a dataframe
    '''

    engine = establish_conection(password='gr@vityI13')

    return sql.read_sql_table(tablename, engine)


df = read_sql_table('IncomeExpenseTransactions')

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

column_rename = {'IncomeExpenseReportId': 'IncExpId', 'CaseFileReportId': 'CasFil',
                 'TransactionDate': 'TranDt',
                 'TransactionCategoryId': 'TranCat', 'CourtOrderTransaction': 'CourtOrdTran',
                 'ProtectedPersonLivesAtCareFacility': 'CarFac'}

df.rename(columns=column_rename, inplace=True)

df['Expense'] = df['IsExpense'].astype(int)
df['CarFac'] = df['CarFac'].astype(int)
df['CourtOrdTran'] = df['CourtOrdTran'].astype(int)

del df['CreateUserId']
del df['LastModUserId']
del df['LastModDate']
del df ['CheckNumber']
del df['Amended']
del df['TrustName']
del df['IsIncome']
del df['IsExpense']


# Remove transactions which are either 'Transfer to Trust' (id=245) or 'CAAP Audit
# Expense Adjustment' (id=249)


df2 = read_sql_table('TransactionCategories')

d_tran = {}

trans_cat = df2['TransactionCategoryId'].unique()
for i in xrange(len(trans_cat)):
    d_tran[df2.iloc[i]['TransactionCategoryId']] = df2.iloc[i]['Description']

df['TranDescr'] = df['TranCat'].map(d_tran)

df = df[(df['TranCat']!= 245) & (df['TranCat']!= 249)]

columns_to_keep = ['IncExpId', 'CasFil', 'Amount', 'TranDt', 'TranCat', 'TranDescr', 'CourtOrdTran', 'CarFac' ]

# Use only those transactions where money is spent, Expense == 1, and not Expense==0
# Use the data for which datetime information is sensible
df = df[(df['Expense']==1) & (df['TranDt']> datetime.date(year=2010,month=1,day=1))
        & (df['TranDt']<datetime.date(2016, 1, 1))][columns_to_keep]

df['NumDays'] = (df['TranDt'] - df['TranDt'].min())/ np.timedelta64(1,'D')

df.to_csv('expense.csv')

'''
For feature engineering
'''

df['TranDt'] = pd.to_datetime(df['TranDt'])

duration = df.groupby(by='CasFil')['NumDays'].max() - df.groupby(by='CasFil')['NumDays'].min()
NoCount = df.groupby(by='CasFil')['Amount'].count()
Total = df.groupby(by='CasFil')['Amount'].sum()

raw = {'Duration': list(duration), 'NumDataPts' : list(NoCount), 'Total' : Total}
explore = pd.DataFrame(raw, columns = ['Duration', 'NumDataPts',  'Total'], index=NoCount.index)
explore.reset_index(level=0, inplace=True)

# Create a pivot dataframe to count number of transactions in each Category
# If there is no trasaction of certain category, df_pivot.fillna(value=0)

df_piv = df.pivot_table(values=['Amount'], index=['CasFil'], columns='TranCat', aggfunc='count')
df_piv.fillna(0, inplace=True)

# Add more columns to this pivot dataframe
df_piv['CasFil'] = df_piv.index
df_piv = pd.merge(df_piv, explore, how='outer', left_on='CasFil', right_on='CasFil')
del df_piv[df_piv.columns.tolist()[-5]]
df_piv.to_csv('expense_matrix.csv')
