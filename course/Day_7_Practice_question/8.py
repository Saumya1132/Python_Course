# list of dictionaries find dictionaries with the highest value for a specific key

data = [
    {'name': 'John', 'age': 25, 'score': 90},
    {'name': 'Alice', 'age': 30, 'score': 85},
    {'name': 'Bob', 'age': 28, 'score': 95},
    {'name': 'Charlie', 'age': 32, 'score': 88}
]

key = 'score'

highest_value_dicts = [dict for dict in data if dict[key] == max(dict[key] for dict in data)]

print(highest_value_dicts)