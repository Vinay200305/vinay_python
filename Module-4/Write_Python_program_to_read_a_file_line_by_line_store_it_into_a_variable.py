#Write a Python program to read a file line by line store it into a variable


f = open('first.txt','r')   
lines = f.readlines()  


for i in lines:
    line = i    
    print(line)     