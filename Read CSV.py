import pandas as pd
import matplotlib.pyplot as plt
file = 'C:/Users/celin/OneDrive/Desktop/Learning/python/ImportandCleandatainPython1/titanic_sub.csv'
#read first 5 rows,header mustbe integer or list of integer 2 ways of reading header of dataframe
df=pd.read_csv(file,nrows =5, header=0)
print(list(df))
print(df.head())

#convert pandas dataframe to numpy array
df_nparray=df.as_matrix()
print(type(df_nparray))
data =pd.read_csv(file)

#histgram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

