
#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

list1 = []    

n = int(input("Enter number of element : "))    

for i in range(n):
    element = int(input(f"Enter {i+1} element : "))  
    list1.append(element)  

print("Your List Is : ",list1)   
minimum = min(list1)   
maximum = max(list1)   

print(f"Minimum number : {minimum}")    
print(f"Maximum number : {maximum}")    
