# Comparison Operators
# Used with decision aking. If Statements, IF..Else,Nested If
marks =int(input("Enter your marks: \n"))
# If Else deals with only a single condition
if marks<50:
    print (marks)
    print("Failed")
    print("You repeat Class")
    if marks <32:                       # Nested If
        print ("Extreme failure")

elif marks>=50 & marks <60:
    print("Passed with an Average")
elif marks >=60 and marks < 70:
    print("Passed")
elif marks >= 70 and marks < 100:
    print("Passed")
else:
    print('Please Re-enter your marks')




