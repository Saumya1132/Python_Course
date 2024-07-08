# Name starting with  A

names = ['Alice', 'Bob','Ashish', 'Charlie', 'David', 'Eve', 'Frank', 'apple', 'banana']

new_list = []

for name in names:
    if name[0].lower() == 'a':
        new_list.append(name)

print(new_list)