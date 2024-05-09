
#Write a Python program to replace last value of tuples in a list.

tuple1 = []     

n = int(input("Enter number of tuple : "))   
for i in range(n):
    input_element = input(f"Enter {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))    

print(tuple1)   
updated_value = input("Enter update value : ")   
for i in range(len(tuple1)):
    upd_list = list(tuple1[i])      
    upd_list[-1] = updated_value   
    tuple1[i] =tuple(upd_list)      

print(tuple1)   
