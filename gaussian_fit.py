'''
cruve fitting with gaussian function
'''
from dataprocess import DataProcess
import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)
# load data
path = "E:\\PythonProjects\\AnomalyDetection\\data\\5minStepsWithRealID-iphone00.csv"
df = pd.read_csv(path)
df[' date'] = pd.to_datetime(df[' date'])
print(df)
userlist = df[' user ID'].unique()
print(userlist)
userid = userlist[5]
df_user = df.loc[df[' user ID'] == userid]

total_days = df_user.shape[0]
print("days:",total_days)

dp = DataProcess(flag=True,input_df=df_user)
df_prior = dp.setup()
print(df_prior)
