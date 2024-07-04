#Write a Python program to count the frequency of words in a file.

word_freq = {}      


f = open('first.txt', 'r')     

for line in f:  
    words = line.split()  
    for word in words:                
        word = word.strip('.,?!;:"') 
        word = word.lower()    
        word_freq[word] = word_freq.get(word, 0) + 1    


print("Word frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")    