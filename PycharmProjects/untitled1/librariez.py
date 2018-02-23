import numpy
import pan

data =pandas.read_csv('sample.csv') #Reading a file using pandas
print(data)
print(deta.describe()) # It shpw he mean. median , max and so on.
sort = data.sort_values(['Female'],ascending =True) #Sorting Values
print(sort) #female appears in ascending order
#ascending  False means descending
print (data[['Male']]).mean()) #Will print only the mean of the list of the male
print (data[['Male']]) #Will print only the list of the male

#Check on pygal