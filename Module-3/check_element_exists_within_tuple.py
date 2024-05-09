#Write a Python program to check whether an element exists within a tuple.

list1 = []  

n = int(input("Enter number of element : "))    

for i in range(n):
    list_input = input("Enter a element : ")
    list1.append(list_input)    

tuple1 = tuple(list1)   

element = input("Enter a element to check : ")  
if element in tuple1:   
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exists in the tuple.")