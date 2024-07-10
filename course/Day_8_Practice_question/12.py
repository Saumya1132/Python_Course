# create a new text file and write some text

def create_text_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Text file '{file_path}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
create_text_file('example.txt', 'This is an example text.')