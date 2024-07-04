#Write a Python class named Circle constructed by a radius and two methods which will compute the area and 
#the perimeter of a circle 




class Circle:   #create class
    def set_radius(self, radius):   #create function
        self.radius = radius    
        
    def calculateArea(self):
        self.area = 3.14 * self.radius * self.radius    #calculate area of circle
        
    def calculate_perimeter(self):  
        self.perimeter = 2 * 3.14 * self.radius     #calculate perimeter of circle
        
circle = Circle()   
radius = int(input("Enter the  radius of a circle : "))  #get value from user
circle.set_radius(radius)   
circle.calculateArea()      
circle.calculate_perimeter()

print("Area of the circle : ",circle.area)      #display area of circle
print("Perimeter of the circle : ",circle.perimeter)    #display perimeter of circle
