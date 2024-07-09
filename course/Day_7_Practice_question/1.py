# dict to store name , age, and address
person_info = {
    "name": "",
    "age": 0,
    "address": ""
}

# User input
person_info["name"] = input("Enter name: ")
person_info["age"] = int(input("Enter age: "))
person_info["address"] = input("Enter address: ")

# Print output
print("Person Details")
print("Name:", person_info["name"])
print("Age:", person_info["age"])
print("Address:", person_info["address"])