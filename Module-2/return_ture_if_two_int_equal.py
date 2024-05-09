#Write a Python program that will return true if the two given integer values are equal or their sum or 


number1=int(input("Enter 1 number : "))     
number2=int(input("Enter 2 number : "))

sum=number1+number2     
print("Sum : ",sum)    
difference=number2-number1      
print("Difference : ",difference)   

if number1==number2 or sum==5 or difference==5:     
    print("True")
else:
    print("False")