#Write a Python program to append text to a file and display the text.

f = open('first.txt','a')   
user_input = input("Enter Append Text : ")      
f.write(f"\n{user_input}")  

f1 = open("first.txt",'r') 
file_content = f1.read()    
print(file_content)    
