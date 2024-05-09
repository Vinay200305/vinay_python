#Write a Python program to convert a list of tuples into a dictionary. 

tuple1 = []     

n = int(input("Enter number of tuple : "))      
for i in range(n):
    input_element = input(f"Enter a {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))     

print(tuple1)  

if n>=2:
    print(dict(tuple1))