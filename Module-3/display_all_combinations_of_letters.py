#Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary.  
#Sample data: {'1': ['a','b'], '2': ['c','d']}

data = {'1': ['a', 'b'], '2': ['c', 'd']}   
result = []

for i in data['1']:
    for j in data['2']:
        result.append(i+j) 

print(result)   