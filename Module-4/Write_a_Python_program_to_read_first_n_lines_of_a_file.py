#Write a Python program to read first n lines of a file.



f = open("first.txt","r")   
user_input = int(input("Enter Number Of Lines : ")) 


for i in range(user_input):
    lines = f.readline()    
    print(lines)    
