#Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(s):   
    
    cleaned_s = ''  
    for char in s:
        if char.isalnum():  
            cleaned_s += char.lower()   


    reversed_s = ''    
    for char in cleaned_s:
        reversed_s = char + reversed_s  
    if cleaned_s == reversed_s:
        print("The string is a palindrome.")    
    else:
        print("The string is not a palindrome.")


string = input("Enter a string: ")  
is_palindrome(string)       