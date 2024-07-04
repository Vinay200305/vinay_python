# What relationship is appropriate for Course and Faculty?

class Faculty:  #create class
    def getData(self, faculty_name):    
        self.faculty_name = faculty_name
        print("Faculty Name:", self.faculty_name)   #display faculty name

class Course(Faculty):
    def getCourse(self, course_name):   
        self.course_name = course_name
        print("Course Name:", self.course_name)     #display course name

c1 = Course()   #create object

facultyname = input("Enter the name of an Faculty  : ")      #get value from user
coursename = input("Enter thr name of the Course : ")

c1.getData(facultyname)   
c1.getCourse(coursename)
