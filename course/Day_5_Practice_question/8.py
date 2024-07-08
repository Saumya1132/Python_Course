# longest word length

def longest_word_length(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return len(longest)

sentence = "Write a Python program to find the length of the longest word in a sentence."
print(longest_word_length(sentence))  
