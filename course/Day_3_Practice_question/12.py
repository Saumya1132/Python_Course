# count number of words with more than five characters in list


words = ["hello", "world", "hi", "how about", "about", "home", "there are", "and"]

# Filter words with more than 5 characters
filtered_words = [word for word in words if len(word) > 5]

print(filtered_words)