# Write your solution here
from random import choice
from string import ascii_lowercase

def generate_password(length: int):
    password = ''
    for i in range(length):
        password += choice(ascii_lowercase)
    
    return password


if __name__ == "__main__":
    
    for i in range(10):
        print(generate_password(2))

