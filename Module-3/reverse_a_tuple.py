
#Write a Python program to reverse a tuple.

list1 = [] 

n = int(input("Enter a element : "))  

for i in range(n):
    input_element = input("Enter an element : ")
    list1.append(input_element)    

print("Tuple is : ",tuple(list1))
list1.reverse()    
reversed_tuple = tuple(list1)   
print(f"Reversed Tuple : {reversed_tuple}")    
