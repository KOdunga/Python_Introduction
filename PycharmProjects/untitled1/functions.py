# functions : It s a block of code that executes a task. Defined by the word def functionName
#  A function has to beinvoked, triggered, called, used to run
def Area(length, width=8):
    area = length * width
    return area
print(Area(4,5))


def save_Record(z,y):
    name=  input("Enter Your Name")
    age = int(input("Enter Your Age"))
    salary = z#int(input("Enter Your Salary"))
    tax = y# float(input("Enter Your Tax"))
    if salary < z:
        print("You get 2000 KES Bonus")
    elif tax < y:
        print("You get 4000 Points")
    else:
        print("OK")

save_Record(2000,2.4)

# Functions can accept parameters


#def sum(r,t): # R and T are parameters passed to function sum
