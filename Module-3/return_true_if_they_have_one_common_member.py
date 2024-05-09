# Write a Python function that takes two lists and returns true if they have at least one common member.

def have_common_member(list1, list2):   
    for element in list1:
        if element in list2:
            print(f"one common member is : {element}") 
            return True
    return False

list1 = []  
n1 = int(input("Enter list1 number of element : "))   

for i in range(n1):     
    element1 = input("Enter element : ")
    list1.append(element1)  

list2 = []  
n2 = int(input("Enter list2 number of element : "))

for i in range(n2):
    element2 = input("Enter element : ")
    list2.append(element2) 

if have_common_member(list1, list2):    
    print("true")
else:
    print("false")