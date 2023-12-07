import numpy as np
import pandas as pd
df=pd.read_csv("D:/Machine Learning/thuc hanh/laptops.csv")
# kiem tra thong tin du lieu
# data_infor=data.info()
# x=data.iloc[:,22:23]
# print(x)
from sklearn.impute import SimpleImputer
variables = []
dtypes = []
count = []
unique = []
missing = []


for item in df.columns:
    variables.append(item)
    dtypes.append(df[item].dtype)
    count.append(len(df[item]))
    unique.append(len(df[item].unique()))
    missing.append(df[item].isna().sum())

output = pd.DataFrame({
    'variable': variables, 
    'dtype': dtypes,
    'count': count,
    'unique': unique,
    'missing': missing, 
   
})    

output.sort_values("missing",ascending=False).reset_index(drop=True)
df.OpSys = df.OpSys.fillna('others')
print(df.info())