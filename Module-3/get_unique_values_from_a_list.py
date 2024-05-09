
#Write a Python program to get unique values from a list

list1 = []  

n = int(input("Enter a number of element : "))      

for i in range(n):
    input_element = input("Enter a element : ")
    list1.append(input_element)    

unique_value = set(list1)   
print("Unique value : ",list(unique_value))     
