# What relationship is appropriate for Student and Person?

class Person:   #create class
    def setData(self, name):    #create method
        self.name = name
        print("Name:", self.name)   #display PersonName

class Stud(Person):  #create class
    def setStudentID(self, stud_id):     #create method
        self.student_id = stud_id
        print("Student ID:", self.stud_id)   #display student id

stud = Stud() #create object

name = input("Enter the name of the Student  ")    #get value from user
stud_id = input("Enter the ID of the Student  ")

stud.setData(name)   #call function
stud.setStudID(stud_id)
