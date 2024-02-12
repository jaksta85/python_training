import pandas as pd
import numpy as np
import os
import time
import datetime as dt

#df1 = pd.read_csv('C:\Kuba\Python\Countries.csv')

files = [file for file in os.listdir(r'C:\Kuba\Python\venv\sales_data')]
df_all = pd.DataFrame()

for file in files:
    df = pd.read_csv(r'C:\Kuba\Python\venv\sales_data' + '\\' + file)
    df_all = pd.concat([df_all,df])

df_all = df_all[df_all['Order Date'] !='Order Date']
df_all['Order Date'] = pd.to_datetime(df_all['Order Date'])
df_all['month'] = pd.DatetimeIndex(df_all['Order Date']).month
df_all['sales'] = df_all['Quantity Ordered'].astype(float) * df_all['Price Each'].astype(float)

df = df_all.groupby(['month'])['sales'].sum().reset_index()
df = df.sort_values("sales",ascending=False)
print(df)
print(df.loc[0:0,"month"])
print("AA")
