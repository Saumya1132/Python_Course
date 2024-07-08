# variables for storing persons names,age and average test scores

persons = []

while True:
    name = input("Enter person's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break

    age = int(input("Enter person's age: "))
    test_score = float(input("Enter person's average test score: "))

    persons.append({'name': name, 'age': age, 'test_score': test_score})

print("Persons' data:", persons)