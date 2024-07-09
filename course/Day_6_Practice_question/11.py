# check list is in the ascending order or not

def is_ascending(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

lst = [14, 2, 3, 44, 5]

if is_ascending(lst):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")