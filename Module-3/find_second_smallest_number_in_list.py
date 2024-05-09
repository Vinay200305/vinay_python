#Write a Python program to find the second smallest number in a list.
list1 = []
n = int(input("Enter number of element : ")) 

if n!=0:
    for i in range(n):
        list1_input = int(input("Enter a number : "))   
        list1.append(list1_input)   

    print(list1)
    lowest = min(list1)     
    list1.remove(lowest)    

    second_lowest = min(list1)  
    print("Second smallest element is : ",second_lowest)    
else:
    print("Enter valid number of element.")