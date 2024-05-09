
#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def printUniqueElement(input_element): 
    unique_elements = set(input_element)  
    print(list(unique_elements)) 

list1 = []

n = int(input("Enter the number of elements: ")) 
 
for i in range(n):
    input_element = input("Enter an element: ")
    list1.append(input_element) 

printUniqueElement(list1)  
