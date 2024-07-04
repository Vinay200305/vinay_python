#Write a Python program to count the number of lines in a text file.



f = open('first.txt','r')   


lines = f.readlines()   
line = []   


for i in lines:
    line.append(i)      



line_count = len(line)     
print(line_count)   