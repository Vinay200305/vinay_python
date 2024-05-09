#How Do You Check The Presence Of A Key In A Dictionary?

dict1 = {} 

n=int(input("Enter number of dict1 pairs : "))  
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    

key_check = input("Enter check key name : ")    

if key_check in dict1:
    print(f"The key {key_check} Presence in the dictionary.")    
else:
    print(f"The key {key_check} dose not Presence in the dictionary.")  