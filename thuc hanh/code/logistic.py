import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#  tao du lieu mau
hours_studied=np.random.normal(5,1,100)
exam_result=(hours_studied+np.random.normal(0,1,100))>5

print(hours_studied)
print(exam_result)

#  chia du lieu thanh tap huan luyn va tap kiem thu
X_train,X_test,y_train,y_test=train_test_split(hours_studied.reshape(-1,1),exam_result,test_size=0.2,random_state=42)

#  khoi tao va huan luyen mo hinh
model=LogisticRegression()
model.fit(X_train,y_train)

#  du doan tap kiem thu
y_pred=model.predict(X_test)

#  danh gia mo hinh
accuracy=accuracy_score(y_test,y_pred)
print(f'accurary:{accuracy:2f}')

#  ve do thi truc quan hoa du lieu 
plt.figure(figsize=(10,6))  
plt.scatter(X_test,y_test,color='black',label='Actual')
plt.scatter(X_test,y_pred,color='red',marker='x',label='Precdicted')
plt.title('Logistic Regresstion Example')
plt.xlabel('Hours studies')
plt.ylabel('pass/fail')
plt.legend()
plt.show()