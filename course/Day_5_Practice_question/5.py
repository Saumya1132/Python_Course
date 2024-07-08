# Sentence as input counts number of words

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter Sentence: ")
print(count_words(sentence))  
