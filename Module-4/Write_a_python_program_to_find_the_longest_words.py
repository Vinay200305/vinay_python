#Write a python program to find the longest words.


f = open("first.txt",'r')   


max_length = 0  
longest_word = ""   


for line in f:
    words = line.strip().split()    
    for word in words:
        if len(word) > max_length:
            max_length = len(word)  
            longest_word = word 
        elif len(word) == max_length:   
            longest_word += " " + word



print("Longest word : ",longest_word)   