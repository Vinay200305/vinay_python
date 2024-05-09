#Write a Python script to concatenate following dictionaries to create a new one.

dict1 = {}  

n=int(input("Enter number of dict1 pairs : "))
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    

dict2 = {} 
n=int(input("Enter number of dict2 pairs : ")) 
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")   
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    

concate_dict = {}   
list1 = [dict1, dict2]
for i in list1: 
    for key, value in i.items():    
        concate_dict[key] = value   

print("concatenate dictionaries : ",concate_dict)    