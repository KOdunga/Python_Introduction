# Program to calculate netsalary from gross salary

grosssalary     = float(input("Enter your Salary: \n"))                       # Capture gross salary
waterallowance  = float(input("Enter your water allowance: \n"))              # Capture gross salary
houseallowance  = float(input("Enter your house allowance: \n"))              # Capture gross salary
if grosssalary < 10000.0:
    nssf = 200.0
else:
    nssf = 250.0
#nssf            = int(input("Enter your nssf pay: \n"))                     # Capture gross salary
salary          = 0.7*grosssalary                                           # Factor in taxes
netsalary       = float(salary + waterallowance + houseallowance - nssf)      # Get the net calculation
print("The net salary is", netsalary)                                       # Print the net salary


