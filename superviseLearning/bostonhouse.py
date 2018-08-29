import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


boston=pd.read_excel('C:/Users/celin/OneDrive/Desktop/Learning/python/superviselearning/bostonhousing.xls')
print(boston.head())

#to use scikit learn, we need 'feature and target values in distinct array, X and Y

#drop the target
X = boston.drop('MV',axis=1).values
#we keep only the target
Y = boston['MV'].values

X_rooms=X[:,5]
type(X_rooms),type(Y)

#reshape the numpy array into desire shape, keep the first dimension and add another dimension of sie one to X
Y=Y.reshape(-1,1)
X_rooms= X_rooms.reshape(-1,1)
plt.scatter(X_rooms, Y)
plt.ylabel('Value of house/1000 ($)')
plt.xlabel('Number of rooms')
#more roome the higher price of the house
plt.show()

reg=linear_model.LinearRegression()

reg.fit(X_rooms,Y)
prediction_space=np.linspace(min(X_rooms),max(X_rooms)).reshape(-1,1)

plt.scatter(X_rooms,Y,color='blue')
plt.plot(prediction_space,reg.predict(prediction_space),color='black',linewidth=3)
plt.show()







