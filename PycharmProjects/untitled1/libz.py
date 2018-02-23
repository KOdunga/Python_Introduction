import pandas
print (dir(pandas))
data = pandas.read_csv('sample.csv')
print(data)
print(data.describe())
sort = data.sort_values(['Female'],ascending =True)
print(sort)
print ((data[['Male']]).mean())