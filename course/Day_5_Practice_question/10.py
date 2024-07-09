# list of names find name starting with vowel and print total count

vowels = ['a', 'e', 'i', 'o', 'u']
names = ["sam","kevin","tirth","elish","ashish","om","imo","uno"]

count = sum(1 for name in names if name[0].lower() in vowels)
print(f"Total count of names starting with a vowel: {count}")
    