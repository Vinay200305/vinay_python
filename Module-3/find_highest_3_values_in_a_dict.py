#Write a Python program to find the highest 3 values in a dictionary.

data = {}   
list1 = []  
n = int(input("Enter number of pairs:"))

for i in range(n):
    key=input("Enter Key's:")   
    value=input("Enter Value's:")  
    list1.append(value)    
    data[key] = value   

print("Dictionary : ",data)     

for i in range(3):
    max_number = max(list1)     
    print(f"The {i+1} maximum number in the dic is :", max_number)  
    list1.remove(max_number)
    