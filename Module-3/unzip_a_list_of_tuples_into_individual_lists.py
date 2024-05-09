
#Write a Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]    

list1 = []
list2 = []

for tuple1 in list_of_tuples:
    list1.append(tuple1[0])   
    list2.append(tuple1[1])   
print("First elements:", list1) 
print("Second elements:", list2)
