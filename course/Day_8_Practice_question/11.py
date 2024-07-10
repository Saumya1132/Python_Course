# read the text file and print it contents

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
        print("File read successfully!")
    except FileNotFoundError:
        print("The specified file does not exist.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

# Example usage

file_path = "D:\course\Day_8_Practice_question\source.txt"
read_file(file_path)