# importing a module
import math,statistics
# To import an alias use as
#Import math as m
#import maxnumber as m

# Check the imported "module" functions using dir


print(dir(math))
#print (dir(m))
print(math.cos(180))
print(math.sqrt(25))
print (math.factorial(7))
print (type(math.trunc(5.76474)))
print(dir(statistics))

scores =[56,66,75,68,98,78,67,90,87,34,98]
print(statistics.mean(scores))
print (statistics.stdev(scores))
print(statistics.variance(scores))
k = statistics.mode(scores)
print("Mode: ",k)