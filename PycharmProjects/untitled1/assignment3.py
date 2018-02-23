#write a python program which creates class student (Rollno,name,number of subjects, marks of each subject(list), fees paid).
#Write a parameterized constructor which initializes roll no, name and number of  subjects and create the array of marks, fees
#print(paid)

#display the details of the studet
#display the total marks of the student and average
#display th fee balance  - total fee =10000
#student can pay fees if the have not cleared.

# The user should be able to input some of the values.

class Student:
    def __init__(self,rollno,name,subject_no, marks,fees_paid):
        self.rollno = rollno
        self.name = name
        self.subject_no = subject_no
        self.marks = marks
        self.fees_paid = fees_paid

    def disp(self):
            print("------- Student Details--------")
            print( self.rollno)
            print(self.name)
            print(self.subject_no)
            print(self.marks)
            print(self.fees_paid)

    def marks(self,subject_no,marks):
        print("The student is sitting for \t",stud.subject_no," Subjects")
        print ("The average marks is\t", stud.marks/stud.subject_no)



stud = Student(1001, "Kennedy",4,[45,67,89,64],4000)
stud.disp()
stud.marks()
