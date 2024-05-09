
#Write a Python program to count the number of strings where the string length is 2 or more and the first and 
#last character are same from a given list of strings.

list1 = []  
n = int(input("Enter number of string : "))   

for i in range(n):
    string = input("Enter a string : ")
    list1.append(string)    

count = 0   

for i in list1:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1      

print("Number of strings where first and last character are same : ", count)
