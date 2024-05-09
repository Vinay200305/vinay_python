#Write a Python program to calculate surface volume and area of a cylinder.

radius = float(input("Enter the radius of the cylinder: "))     

height = float(input("Enter the height of the cylinder: "))
pi = 3.24 

surface_area = 2 * pi * radius * (radius + height) 

volume = pi * radius ** 2 * height 

print("Surface Area of the cylinder : ", surface_area)    
print("Volume of the cylinder : ", volume)      