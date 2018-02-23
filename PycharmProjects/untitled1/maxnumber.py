# Create a function that requests for three integers then get the maximum number
def getnumbers():
    list = []
    x = 1
    while x<4:
        num = input("Enter a number: ")
        list.append(num)
        x+=1
    getmaxnum(list)


def getmaxnum(list):
    print(max(list))
y=1
while y != 0:
    getnumbers()
    y = int(input("To exit enter 0, press other numbers to continue: \t"))