#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 

input_string = input("Enter a string: ")    

if len(input_string) < 2:
    result = ""    
else:
    result = input_string[0:2] + input_string[-2:]

print("Result:", result)   