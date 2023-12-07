import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("./laptops.csv")

# 1. In ra thông tin 
print(df)

# 2. Làm sạch dữ liệu
# Tap du lieu ban dau
df.info()

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

# Xử lý các giá trị bị thiếu trong OpSys
# Kiểm tra phân loại các giá trị trong OpSys
print(df.OpSys.value_counts())

# Điền vào các giá trị còn thiếu bằng 'Others'
df.OpSys = df.OpSys.fillna('others')

# Kiểm tra lại tập dữ liệu
df.info()

# 3. Tích hợp dữ liệu
df['Memory'] = df.apply(lambda row: row['hdd'] + row['ssd'], axis=1)
print(df['Memory'])

# 4. Chuyển đổi dữ liệu
# In ra cột chứa dữ liệu cần chuyển đổi
print(df["touchscreen"])

df['touchscreen'] = df['touchscreen'].map({'Yes': 1, 'No': 0})
print(df["touchscreen"])


# 5. Cắt giảm dữ liệu
# In ra danh sách các cột trước khi xóa
print("Các cột trước khi xóa:")
print(df.columns)

# Xóa cột "FlashStorage"
df = df.drop('flashstorage', axis=1)

# In ra danh sách các cột sau khi xóa
print("\nCác cột sau khi xóa:")
print(df.columns)

# dữ liệu sau khi tiền xử lí 
df.to_csv("./laptops_processed.csv", index=False)
