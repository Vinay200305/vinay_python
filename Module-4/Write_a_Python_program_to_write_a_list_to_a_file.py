#Write a Python program to write a list to a file.


list1 = [] 


n = int(input("Enter the number of an elements in list : "))    


for i in range(n):
    element = input(f"Enter {i+1} element : ") 
    list1.append(element)   
    
    
f = open("first.txt","a")   
for item in list1:
    f.write("\n"+list1)    