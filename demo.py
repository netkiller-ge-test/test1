import os

API_KEY = "sk-1234567890abcdef"

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

def read_file(path):
    f = open(path)
    data = f.read()
    return data

def check_login(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query

print(calculate_average([]))
