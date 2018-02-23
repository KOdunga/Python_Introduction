# tuple
points = (23,25,34,56.7,67,34,78,22,90)
print ("I GOT",points[0])       # Prints First Item
print (" WE GOT", points[2:])   # Prints from a specific position+1 upwards
print ("WE HAVE", points[2:6])  # Specify a given range
print ("Points are ", points *2)
# Tuples are static (immutable)
print(points)

#LISTS  Use Square brackets

age = [12,34,23,54,55,67,78,89,67,34]
age.append(34)
print (age)
print ("Age at : ", age[3])
age.insert(4,74)
age.remove(age[3])
print(age)

#DICTIONARY Uses Key and Value approach. Identified by braces.
car = { 'color':'blue',
        'make':'toyota',
        'year': 2011,
        'cost': '430k',
        'reg':'KCF 445Z',
        "TEL":734767689,
        'Location':'Mombasa',
        'year':2016,
        "year":2013}
print (car)
print(car['year'])
print(car['color'])
# Adding and Updating items to a dictionary
car['Mileage']= 900000
car['cost'] = '440k'
print (car)
# Removing an Item, Delete an item, Clear the dictionary, delete the dictionary
#car.pop('year')
#car.clear()
del car['Location']
print (car)
del (car)
print (car)