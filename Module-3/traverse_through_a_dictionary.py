#How Do You Traverse Through A Dictionary Object In Python?

dict1 = {}  

n=int(input("Enter number of dict1 pairs : "))
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    

for keys, values in dict1.items():
    print(keys, ":", values)    