
#Write a Python program to map two lists into a dictionary.

key1 = []  
value1 = []

k1 = int(input("Enter number of key : ")) 
v1 = int(input("Enter number of value : "))

if k1==v1:  
    for i in range(k1):
        input_key = input(f"Enter {i+1} key : ")    
        key1.append(input_key)  
        input_value = input(f"Enter {i+1} value : ")
        value1.append(input_value)  

    list_to_dict = dict(zip(key1, value1)) 
    print(f"List to dictionary : {list_to_dict}") 

else:
    print("Please Enter key and value are equal..!")
