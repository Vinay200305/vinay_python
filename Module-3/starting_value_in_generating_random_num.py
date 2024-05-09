
#How will you set the starting value in generating random numbers?

import random

start = int(input("Enter Starting value : "))
end = int(input("Enter ending value : "))
random.seed(42)     

random_number = random.randint(start,end)   

print(random_number)
