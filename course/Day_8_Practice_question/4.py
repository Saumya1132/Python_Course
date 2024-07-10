# function takes a list of sentences and writes them to new text file each on new line

def write_sentences_to_file(sentences, destination_file):
    try:
        with open(destination_file, 'w') as dest:
            for sentence in sentences:
                dest.write(sentence + '\n')
        
        print(f"Sentences successfully written to {destination_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

sentences = [
    "This is the first sentence.",
    "Here is another sentence.",
    "This is the last sentence."
]
destination_file = 'output.txt'
write_sentences_to_file(sentences, destination_file)
