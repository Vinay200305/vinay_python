#Write a Python program to check multiple keys exists in a dictionary

dict1 = {}  

n=int(input("Enter number of dict1 pairs : "))
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    

keys_check = []    
n2 = int(input("Enter number of check keys : "))  

for i in range(n2):
    input_key = input(f"Enter {i+1} keys : ")
    keys_check.append(input_key)    

print(dict1)
for key in keys_check:
    if key not in dict1:
        print(f"{key} does not exists in a dictionary.")   
    else:
        print(f"{key} exists in a dictionary.")    