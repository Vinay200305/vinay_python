#Write a Python program to convert degree to radian

def degress_to_radian(degrees):     
    pi = 3.14
    radians = degrees * (pi/180)   
    print("degree to radians : ", radians)  

d1 = float(input("Enter the degree : "))    
degress_to_radian(d1)   