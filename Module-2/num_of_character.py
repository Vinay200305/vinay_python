#Write a Python program to count the number of characters (character frequency) in a string

string = input("Enter a string : ")   
count_char = 0 

for char in string:

    if char != " ":
        count_char+=1  

print("Number of character : ",count_char)     