#Write a Python function to check whether a number is perfect or not.

def perfect_number(n):     
    sum = 0    
    for i in range(1, n):
        if n % i == 0:  
            sum += i    
    if sum == n:    
        print("Number Is Perfect.")
    else:
        print("Number Is Not Perfect.")
    

user_input = int(input("Enter Number : "))     
print(perfect_number(user_input)) 