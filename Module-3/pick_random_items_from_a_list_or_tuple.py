
#How can you pick a random item from a list or tuple?

import random

list1 = [] 

n = int(input("Enter number of element : "))    

for i in range(n):
    element = input(f"Enter {i+1} element : ")  
    list1.append(element)   

random_item = random.choice(list1)  
print("Your Random Item Is : ",random_item) 
