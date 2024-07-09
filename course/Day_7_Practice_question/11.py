# Enters list of directories and sort them based on their specified keys

def get_user_input():
    directories = []
    while True:
        dir_name = input("Enter directory name (or type 'done' to finish): ")
        if dir_name.lower() == 'done':
            break
        date_modified = input(f"Enter date modified for {dir_name} (YYYY-MM-DD): ")
        size = float(input(f"Enter size for {dir_name} (in MB): "))
        directories.append({'name': dir_name, 'date_modified': date_modified, 'size': size})
    return directories

def sort_directories(directories, sort_key):
    return sorted(directories, key=lambda x: x[sort_key])

def main():
    directories = get_user_input()
    print("\nChoose a key to sort by: name, date_modified, or size")
    sort_key = input("Enter the key: ")
    if sort_key not in ['name', 'date_modified', 'size']:
        print("Invalid sort key!")
        return
    
    sorted_directories = sort_directories(directories, sort_key)
    print("\nSorted directories:")
    for dir in sorted_directories:
        print(dir)

if __name__ == "__main__":
    main()


