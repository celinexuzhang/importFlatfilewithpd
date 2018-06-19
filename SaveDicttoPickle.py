import pickle

#write python dict to a file
mydict={'a':1,'b':2,'c':3}
output= open('myfile.pkl','wb')
pickle.dump(mydict,output)
output.close()

#Open a pickle file and load data d

file= open('myfile.pkl','rb')
d = pickle.load(file)
file.close()

print(d)
print(type(d))

