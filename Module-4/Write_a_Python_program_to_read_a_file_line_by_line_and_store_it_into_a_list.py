#Write a Python program to read a file line by line and store it into a list.


f = open('first.txt','r')   
lines = []  



for line in f:
    lines.append(line)  
    
    
for line in lines:
    print(line)     

print("\n-----------------------text in  List-----------------------\n")
print(lines)    
