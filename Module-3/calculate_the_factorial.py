#Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):  
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i     
        print("Factorial is : ", result)   

number = int(input("Enter a number : "))   
factorial(number)  