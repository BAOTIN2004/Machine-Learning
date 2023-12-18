from sklearn.preprocessing import MinMaxScaler

# create data

data=[[10,2],[3,7],[0,10],[7,8]]
scaler=MinMaxScaler()
model=scaler.fit(data)
scaled_data=model.transform(data)

print(scaled_data)