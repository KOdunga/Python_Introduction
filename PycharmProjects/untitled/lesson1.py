print(8000)
print("Modcom")
print (7000)
print (5+6)
print ("Hello")#comment

# Rules in a variable:
# 1. No Spacing
# Don not start with a number, you can end with a number
num1 = 30000 # Ths is an int
num2 = 40000
num3 = 50000
num4 = 70000
num5 = 500.5 # This is a float

# Data Types
# Numbers
# String
# List
# Tuple
#Dictionary
print (num1)
print (num2)
print ("I have ",num2, "Shillings")
# (,)Comma Combines a string and a variable

print(2000,"Students")
print("I will look for", num4)
print("I have", num2, "and", num4)
answer = num2 + num1 + num3
print ("My Answer is", answer)
 # Define a new variable called answer
town = "Thika"
print("I will be going to", town)
# Tuple.  Stores a series of numbers, like an array. Brackets () Represent a tuple
# List
# Dictinary
year = (2010,2011,2012,2013,2014,2015,2016,2017,2018,"Not Present")
print (year[-1])
counties = ("Busia","Bungoma","London", "Vihiga")
print (counties [2],year[4])
print (year[:])
print (counties)

#Assignment
#Prompt the user  to enter a Salary, Water Allowance, House Allowance, NSSF, TAX
# Find and Print the net pay
# What is TUPLE?
# What is a LIST
grosssalary = int(input("Enter your Salary"))
waterallowance = int(input("Enter your water allowance"))
houseallowance = int(input("Enter your water allowance"))
nssf = int(input("Enter your water allowance"))
tax = 0.3 * salary
salary = 0.7*netsalary
netsalary = int(salary + waterallowance + houseallowance - nssf)
print("The net salary is", netsalary)