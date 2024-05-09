
#Write a Python program to select an item randomly from a list.

import random 

list1 = []  

n = int(input("Enter a number of element : "))  

for i in range(n):
    element = input(f"Enter {i+1} element : ")
    list1.append(element)      

random_item = random.choice(list1)     
print("Randomly item selected from a list : ",random_item)
