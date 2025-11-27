# Write your solution here
import json
import os


def print_persons(filename: str):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File or Directory: {filename}, dose not exist")
        
    with open(filename, 'r') as f:
        data = json.load(f)

    for person in data:

        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f'{name} {age} years ({hobbies})')

if __name__ == "__main__":
    print_persons("file1.json")
    print_persons("file2.json")
    print_persons("file3.json")
    print_persons("file4.json")