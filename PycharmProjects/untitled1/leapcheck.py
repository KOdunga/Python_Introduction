x=0
while x==0:
    year= int(input("Enter Year:\n"))
    if (((year%4) == 0) and((year%100) !=0)) or (year%400 ==0):
            print("A Leap year")
    else:
        print("It is Not a Leap Year")
    x=int(input("To proceed, enter 0, To Quit, enter 1\n"))

