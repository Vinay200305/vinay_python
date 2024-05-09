#Write python program that swap two number with temp variable and without temp variable.


first_number = int(input("Enter First Number : "))      
second_number = int(input("Enter Second Number : "))    

temp = first_number     
first_number = second_number
second_number = temp

print("---------After swapping value---------")
print(f"First Number : {first_number} \nSecond Number : {second_number}")     


first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("---------After swapping value---------")
print(f"First Number : {first_number} \nSecond Number : {second_number}")   