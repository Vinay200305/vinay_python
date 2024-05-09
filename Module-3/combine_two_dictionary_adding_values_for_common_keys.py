#Write a Python program to combine two dictionary adding values for common keys. 
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

dict1 = {}  
n=int(input("Enter number of dict1 pairs : ")) 
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")  
    value1 = input(f"Enter {i+1} Values : ")
    if value1.isdigit():
        value1 = int(value1) 
        dict1[key1] = value1
    else:
        dict1[key1] = value1

dict2 = {} 
n=int(input("Enter number of dict2 pairs : ")) 
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")   
    value1 = input(f"Enter {i+1} Values : ")
    if value1.isdigit():
        value1 = int(value1)
        dict2[key1] = value1
    else:
        dict2[key1] = value1


combined_dict = {}     

for key, value in dict1.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

for key, value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print(dict1)    
print(dict2)    
print("Combined dictionary : ", combined_dict)      