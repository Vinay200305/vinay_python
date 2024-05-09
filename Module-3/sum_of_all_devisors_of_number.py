
#Write a Python program to returns sum of all divisors of a number

def divisors_list(number):      
    divisors = []      
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)  
    return divisors

numbers = input("Enter a list of numbers separated by spaces : ").split() 

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for num in numbers:
    divisor_list = divisors_list(num)

print(f"Divisors number are : {divisor_list}") 

for num in numbers:
    divisors = divisors_list(num)
    sum_of_divisors_result = sum(divisors)  

print(f"Sum of divisors number : {sum_of_divisors_result}")     
