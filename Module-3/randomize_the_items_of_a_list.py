
#How will you randomizes the items of a list in place?
import random

my_list = [1,2,3,4,5,6,7]  

n = int(input("Enter number of element : "))
for i in range(n):
    user_input = input(f"Enter {i+1} element : ")
    my_list.append(user_input)

random.shuffle(my_list) 

print(my_list)  
