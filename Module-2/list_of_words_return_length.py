#Write a Python function that takes a list of words and returns the length of the longest one.

number = int(input("Enter total number of words : "))  
wordList = []
maxlength = 0
longest_words = []

for word in range(number):
    word = input(f"Enter {word+1} word : ")
    wordList.append(word)       

for word in wordList:
    if len(word) > maxlength:     
        maxlength = len(word)       
        longest_words = [word]     
    elif len(word) == maxlength:         
        longest_words.append(word)      

print("Longest word :", longest_words)