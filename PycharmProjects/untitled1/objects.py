# An object has a state and a behavior.
class Account:  # defining a constructor

    # Initalize the object
    def __init__(self,acno,amount,name,type):
        self.acno = acno
        self.amount =amount
        self.name = name
        self.type = type

        #Passing a parameter that holds deposited cash
    def deposit(self,depamount):
        if depamount < 50:
            print("Below Deposit threshold")
        elif (depamount > 50000):
            print("Too Much, not allowed!")
        else:
            self.amount = self.amount + depamount
            print("Deposit of :", depamount, "Succesful")
            print("Current Balance: ", self.amount)

    def checkdetails(self):
        print("------- Account Details--------")
        print(self.acno)
        print(self.amount)
        print(self.type)
        print(self.name)
        print(self.amount)

    def changetype(self,type):
        self.type = type
        print("Account Type Changed to", self.type)



    def withdraw(self,withamount):
        if (withamount > 50000):
            print("Not Allowed")
        elif (withamount> self.amount):
            print("Insufficient Balance")
        else:
            self.amount = self.amount - withamount
            print("Withdrawal of ", withamount," Successful")
            print("Current Balance: ", self.amount)


    def check_bal(self):
        print("Current Balance: ",self.amount)

ob = Account(10003,50000,"Joe", "Personal")

def launcher():
    print("1.   Check balance")
    print("2.   Deposit")
    print("3.   Withdraw")
    print("4.   Change Account Type")
    print("5.   Check Details")

    y = int(input("Option: \t"))

    if y==1:
        ob.check_bal()

    elif y == 2:
        x = int(input("How Much do you want to Deposit:\t"))
        ob.deposit(x)

    elif y==3:
        x = int(input("How Much do you want to Withdraw:\t"))
        ob.withdraw(x)
    elif y == 4:
        ob.changetype("Yeah")
    elif y == 5:
        ob.checkdetails()
    else:
        print("Unavailable option")
start =0
while start != 1:
    start = int(input("To Exit, Enter 1, To Continue, Enter 0"))
    launcher()
