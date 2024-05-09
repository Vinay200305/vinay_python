#Write a Python program to check whether a list contains a sub list.

main_list = []  
sublist = []

n = int(input("Enter main list number of element : ")) 
n1 = int(input("Enter sublist number of element : "))

for i in range(n):
    element = input(f"Enter {i+1} main list element : ")
    main_list.append(element)   
    
for i in range(n1):
    element = input(f"Enter {i+1} sublist element : ")
    sublist.append(element)    


main_set = set(main_list)
sublist_set = set(sublist)


contains_sublist = sublist_set.intersection(main_set) == sublist_set

print(contains_sublist)  