#Write python program that user to enter only odd numbers, else will raise an exception.

try:
    num = int(input("Please enter an odd number: "))    #get value from user
    
    if num % 2 != 0:     #check number is even or odd
        print(f"You entered : {num} is odd")
    else:
        raise Exception("You entered an even number. Please enter an odd number.")

except Exception as e:
    print(e)
