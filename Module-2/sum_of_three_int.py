#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

number1=int(input("Enter 1 Number : "))     
number2=int(input("Enter 2 Number : "))
number3=int(input("Enter 3 Number : "))     


if number1==0 and number2==0 or number1==0 and number3==0 or number2==0 and number3==0:
    print("ENTER A VALID VALUE!")
else:
    total=number1+number2+number3
    print("Your Sum is : ",total)