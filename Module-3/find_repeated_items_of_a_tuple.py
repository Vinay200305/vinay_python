
#Write a Python program to find the repeated items of a tuple.

tuple1 = []   
n = int(input("Enter number of element : "))    
for i in range(n):
    input_element = input(f"Enter {i+1} element : ")    
    tuple1.append(input_element)   

print("Your Tuple : ",tuple(tuple1))  

temp = []   
repeated_item = []  

for i in tuple1:
    if i not in temp:
        temp.append(i)      
    else:
        repeated_item.append(i)     

print("Repeated Item : ",tuple(repeated_item))      
