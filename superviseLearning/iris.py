from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

plt.style.use('ggplot')
iris = datasets.load_iris()
#iris data type is bunch, which is key-value pairs
print(type(iris))
print(iris.keys())
print(iris.target_names)

x=iris.data
y=iris.target

df=pd.DataFrame(x,columns=iris.feature_names)
iris_plot=pd.plotting.scatter_matrix(df,c=y, figsize= [8,8],s= 150, marker='D')
plt.show()

#the scikit-learn API requires firstly that you have the data as a Numpy array or pandas Dataframe
#also requires features(independent variable as continuous values, there is no missing value in the data
# Create a k-NN classifier with 6 neighbors
knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(iris['data'],iris['target'])

