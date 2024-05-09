#Write a Python function to get the largest number, smallest num and sum of all from a list.

def get_stats(numbers):     
    max_num = max(numbers)      
    min_num = min(numbers)      
    total_sum = 0   
    for num in numbers:
        total_sum += num       
    return max_num, min_num, total_sum

list1 = []  
n = int(input("Enter number of element : "))  

for i in range(n):
    element = int(input("Enter a element : "))  
    list1.append(element) 

largest, smallest, total_sum = get_stats(list1)
print("\nLargest Number : ",largest)    
print("Smallest Number : ",smallest)    
print("Total sum : ",total_sum)   