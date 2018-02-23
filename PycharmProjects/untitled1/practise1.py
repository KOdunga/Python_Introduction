# Create a function that accepts two parameters, namely;
#  Alist of type string
# A name
# The function should then check if a word is in that list. (Let the word exist e.g THIKA [Busia, Thika, Nakuru, Nyeri])
# Return that word in reverse order if found.
#If the word is not found, append the word and return the list.

def practise(a,b):
    if b in a:
        print(a.reverse())
    else:
        a.append(b)
        print(a)

practise(['Thika', 'Nairobi', 'Busia'],'Thika')

