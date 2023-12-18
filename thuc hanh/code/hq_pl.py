import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import datasets,linear_model

# height
x=np.array([[147,150,153,163,165,168,170]]).T
y=np.array([49,50,51,54,58,59,60])

# fit the model by linear regression
regr=linear_model.LinearRegression()
regr.fit(x,y)
y1=regr.predict(np.array([[155]]))
y2=regr.predict(np.array([[160]]))
# print('input 155cm, true output 52kg, predicted output %.2fkg' %(y1))

#plot data points
plt.scatter(x,y,color='black')

# plot the regression line
plt.plot(x,regr.predict(x),color='blue',linewidth=3)


# add labels and title
plt.xlabel('Height(cm)')
plt.ylabel('Weight(kg)')
plt.title('Linear regression Example')

plt.scatter([[155],[160]],[y1,y2],color="red")
plt.annotate(f'Predicted: {y1[0]:.2f}kg',xy=[155,y1],xytext=[160,y1],arrowprops=dict(facecolor='red',shrink=0.05))
plt.annotate(f'Predicted:{y2[0]:.2f}kg',xy=[160,y2],xytext=[160,y2+2],arrowprops=dict(facecolor='red',shrink=0.05))
plt.show()