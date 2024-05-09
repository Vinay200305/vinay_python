
#Write a Python program to read a random line from a file.

import random

f1 = open('temp.txt','w')  

n = int(input("Enter number of student : "))   
for i in range(n):
    id = int(input(f"Enter {i+1} id : "))  
    name = input("Enter name : ")  
    f1.write(f"Id : {id} \nName : {name} \n")  
f1.close()

r1 = open('temp.txt','r+')       
lines = r1.readline()
random_line = random.choice(lines)
print("Random line from file : ",random_line)
r1.close()
