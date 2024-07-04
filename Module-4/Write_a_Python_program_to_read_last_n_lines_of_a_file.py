#Write a Python program to read last n lines of a file. 

f = open('first.txt','r')   
user_input = int(input("Enter Number Of Lines : "))     
lines = f.readlines()   
last_n_lines = lines[-user_input:]  

for line in last_n_lines:
    print(line)    