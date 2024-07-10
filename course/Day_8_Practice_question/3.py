# read text file and count the number of words and lines

def count_words_and_lines(source_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
            words = contents.split()
            lines = contents.split('\n')
            
            word_count = len(words)
            line_count = len(lines)
        
        print(f"The file contains {word_count} words and {line_count} lines.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = 'D:\course\Day_8_Practice_question\source.txt'
count_words_and_lines(source_file)
