
#How can you pick a random item from a range?

import random

start = int(input("Enter start range : "))
end = int(input("Enter end range : "))

my_range = range(start, end)    


random_item = random.choice(list(my_range))

print("Random item from the range:", random_item)   
