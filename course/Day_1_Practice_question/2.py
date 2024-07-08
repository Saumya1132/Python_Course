# Greetings message

import random

def greet_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    greetings = [
        f"Hello, {name}! You are {age} years young!",
        f"Hey {name}! It's awesome to know you're {age} years old!",
        f"Hi {name}, welcome! {age} is a great age to be!",
        f"Greetings, {name}! You have {age} wonderful years of experience!",
    ]
    greeting_message = random.choice(greetings)
    print(greeting_message)

greet_user()
