#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = []    

n = int(input("Enter number of tuple : "))   
for i in range(n):
    input_element = input(f"Enter a {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))    

print("\n------Display Orignal Tuple------\n",tuple1)

remove_empty = []   
for i in tuple1:
    if i:
        remove_empty.append(i)  
print("\n------Remove Empty Tuple------\n",remove_empty,"\n") 