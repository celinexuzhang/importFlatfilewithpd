#goals: import different datatype flat file using numpy array
#import flat file: basic file contain records(row of fields or attributes) column ( feature and column)
#numpy arrays: standard for storing numberical data , essential for other package

import numpy as np
import pandas as pd


# numpy.loadtxt works well with single data type, but not for mixed data type

#Ex1.1: import text file, skip row 1 and only use column 1 and 3, and import data as "string" data type

filename = 'C:/Users/celin/OneDrive/Desktop/Learning/python/ImportandCleandatainPython1/mnist.csv'
data = np.loadtxt(filename, delimiter = ',', skiprows=1, usecols=[0,2], dtype=str)
print(data)

#Ex2
#np.genfromtxt(), which can handle mixed datatype. If we pass dtype=None to it, it will figure out what types each column should be.
#the first argument is the filename, the second specifies the delimiter , and the third argument names tells us there is a header.
filename1='C:/Users/celin/OneDrive/Desktop/Learning/python/ImportandCleandatainPython1/titanic_sub.csv'
data1= np.genfromtxt(filename1,delimiter=',', names=True, dtype=None)
#Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the flat file imported. You can test this by checking out the array's shape in the shell by executing np.shape(data).
np.shape(data1)
#Acccessing rows and columns of structured arrays is super-intuitive: to get the ith row, merely execute data[i] and to get the column with name 'Fare', execute data['Fare'].
data1['Survived']

#Ex3
# function np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default dtype is None
data2=np.recfromcsv(filename1,delimiter = ',',names = True, dtype = None)
#print the first three entries of the resulting array data2
print(data2[:3])

