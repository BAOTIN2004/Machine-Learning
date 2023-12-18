import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, KBinsDiscretizer

df = pd.read_csv("D:/Machine Learning/thuc hanh/datasets/laptops/laptops.csv")
print(df.head())




# PHẦN 1: LÀM SẠCH DỮ LIỆU (DATA CLEANING)

# 1.1 Xử lý dữ liệu còn thiếu (Missing Value)
# Hiển thị thông tin tổng quan về DataFrame
df.info()

# Tạo các list để chứa thông tin về biến
variables = []
dtypes = []
count = []
unique = []
missing = []

# Lặp qua các cột trong DataFrame
for item in df.columns:
    variables.append(item)
    dtypes.append(df[item].dtype)
    count.append(len(df[item]))
    unique.append(len(df[item].unique()))
    missing.append(df[item].isna().sum())

# Tạo DataFrame để hiển thị thông tin về biến
output = pd.DataFrame({
    "variable": variables,
    "dtype": dtypes,
    "count": count,
    "unique": unique,
    "missing": missing,
})    
# Sắp xếp DataFrame theo số giá trị bị thiếu giảm dần và reset index
output.sort_values("missing",ascending=False).reset_index(drop=True)

# Kiểm tra phân loại các giá trị trong cột OpSys
print(df.OpSys.value_counts())

# Điều kiện 1: Apple là macos
condition_apple = (df["Company"] == "Apple") & pd.isna(df["OpSys"])
df.loc[condition_apple, "OpSys"] = "macos"
# Điều kiện 2: Google là others
condition_google = (df["Company"] == "Google") & pd.isna(df["OpSys"])
df.loc[condition_google, "OpSys"] = "others"
# Điều kiện 3: [Dell Notebook, Acer Notebook, Asus Notebook] là linux
condition_linux = (df["Company"].isin(["Dell", "Acer", "Asus"])) & (df["TypeName"] == "Notebook") & pd.isna(df["OpSys"])
df.loc[condition_linux, "OpSys"] = "linux"
# Các trường hợp còn lại là windows
df["OpSys"] = df["OpSys"].fillna("windows")

# Hiển thị lại thông tin tổng quan về DataFrame sau khi xử lý
df.info()
print(df.OpSys.value_counts())


"-------------------------------------------------------------------------------------------------------------------------------------"
# 1.2 Loại bỏ dữ liệu nhiễu (Noise Data) - Outliers
    # Kiem tra kích thước dữ liệu trước khi xử lí dữ liệu nhiễu
print('dữ liệu trước khi xử lí giá trị ngoaị lai',df.shape)
    # Phát hiện dữ liệu ngoại lai sử dụng percentile
    # Thiết lập giá trị ngưỡng cho dữ liệu
max_weight=df['Weight_kg'].quantile(0.99)
    # Lọc ra dữ liệu ngoại lai
df[df['Weight_kg']>max_weight]
    # Loại bỏ các hàng có chứa giá trị ngoại lai
df=df[df['Weight_kg']<max_weight]





#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PHẦN 2: CHUYỂN ĐỔI DỮ LIỆU (DATA TRANSFORMATION) - CHUẨN HÓA DỮ LIỆU (NORMALIZATION)

# 2.1 Chuyển đổi dữ liệu Categorical thành Numeric
df["Company"] = LabelEncoder().fit_transform(df["Company"])
df["TypeName"] = LabelEncoder().fit_transform(df["TypeName"])
df["touchscreen"] = LabelEncoder().fit_transform(df["touchscreen"])
df["ipspanel"] = LabelEncoder().fit_transform(df["ipspanel"])
df["retinadisplay"] = LabelEncoder().fit_transform(df["retinadisplay"])
df["cpu_brand"] = LabelEncoder().fit_transform(df["cpu_brand"])
df["gpu_brand"] = LabelEncoder().fit_transform(df["gpu_brand"])
df["OpSys"] = LabelEncoder().fit_transform(df["OpSys"])

print(df.head())


"-------------------------------------------------------------------------------------------------------------------------------------"
# 2.2 Chuẩn hóa dữ liệu số (Numeric Scaling)
# 2.2.1 Chuyển đổi đơn vị tiền tệ: Ấn Độ -> VND
ty_gia = 291
df["Price_VND"] = df["Price"]*ty_gia

# 2.2.2 Chuẩn hóa dữ liệu số (Numeric Scaling) - MinMax Scaling
# df["Inches"] = MinMaxScaler().fit_transform(df[["Inches"]])
# df["resolution_width"] = MinMaxScaler().fit_transform(df[["resolution_width"]])
# df["resolution_height"] = MinMaxScaler().fit_transform(df[["resolution_height"]])
# df["cpu_speed"] = MinMaxScaler().fit_transform(df[["cpu_speed"]])
# df["Ram"] = MinMaxScaler().fit_transform(df[["Ram"]])
# df["hdd"] = MinMaxScaler().fit_transform(df[["hdd"]])
# df["ssd"] = MinMaxScaler().fit_transform(df[["ssd"]])
# df["flashstorage"] = MinMaxScaler().fit_transform(df[["flashstorage"]])
# df["hybrid"] = MinMaxScaler().fit_transform(df[["hybrid"]])
# df["Weight_kg"] = MinMaxScaler().fit_transform(df[["Weight_kg"]])
# df["Price"] = MinMaxScaler().fit_transform(df[["Price"]])

# print(df.head())


"-------------------------------------------------------------------------------------------------------------------------------------"
# 2.3 Xử lý dữ liệu văn bản - về văn bản thường

df["cpu_name"] = df["gpu_name"].str.lower()
df["gpu_name"] = df["gpu_name"].str.lower()

print(df.head())


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PHẦN 3: CẮT GIẢM DỮ LIỆU

# Xóa cột indx
df = df.drop("indx", axis=1)
# In ra DataFrame sau khi xóa cột 'indx'
print(df)





#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PHẦN 4: TẬP DỮ LIỆU SAU TIỀN XỬ LÝ
df.to_csv("D:/Machine Learning/thuc hanh/datasets/laptops/laptops_processed.csv", index=False)