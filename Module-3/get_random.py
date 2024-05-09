#How can you get a random number in python?

import random   

range1 = int(input("Enter start range : "))    
range2 = int(input("Enter end range : "))

random_number = random.random()     
print("Random Number : ",random_number)

number = random.randint(range1,range2)  
print("Random Number : ",number)   