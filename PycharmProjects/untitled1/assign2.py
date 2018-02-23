# Create a function that accepts two parameters, namely;
# 1. A list of type string
# 2. A name
# The function should then check if a word is in that list. (Let the word exist e.g THIKA [Busia, Thika, Nakuru, Nyeri])
# Return that word in reverse order if found.
#If the word is not found, append the word and return the list.

counties = ["Nairobi","Mombasa","Thika","Nakuru","Turkana","Garissa","Lamu","Nandi","Bungoma"]
county = "Bungoma"

def checker(a,b):
    if a not in b:
        b.append(a)
        printlist(b)
        return b
    else:
        y = a[::-1]
        print(y)
        return y



def printlist(thelist):
    for i in thelist:
        print (i)
k=0
while k !=1:
    checker(county,counties)
    k = int(input("To continue, press 0, To exit press 1:\t"))
#print (checker(county,counties))
