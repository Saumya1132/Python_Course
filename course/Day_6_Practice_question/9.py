# list of names remove duplicates names from the list

def remove_duplicates(names):
    unique_names = []
    seen = set()
    for name in names:
        if name not in seen:
            seen.add(name)
            unique_names.append(name)
    print(unique_names)       

        
names = ["aman","raham","sam","jeel","drashti","meet","aman","samy","meet","aman"]

remove_duplicates(names)
