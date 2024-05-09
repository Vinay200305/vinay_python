
#Write a Python program to print all unique values in a dictionary.

dict1 = {}
n=int(input("Enter number of dict1 pairs : ")) 
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    


unique_values = set()

for value in dict1.values():
    unique_values.add(value)

print("Unique values in the dictionary : ", unique_values)
