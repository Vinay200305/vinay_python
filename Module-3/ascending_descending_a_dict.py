
#Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {}  

n=int(input("Enter number of dict1 pairs : "))
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    my_dict[key1] = value1    

asc = sorted(my_dict.values())   
desc = asc[-1:]        

print("Value sorted in ascending order:", asc)      
print("Value sorted in descending order:", desc)       
