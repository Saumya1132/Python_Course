# copy data from one file to the other file

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        
        print("File copied successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)
