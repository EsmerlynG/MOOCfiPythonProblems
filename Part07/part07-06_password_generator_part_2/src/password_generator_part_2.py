# Write your solution here
from string import ascii_lowercase, digits
from random import choice, randint, shuffle

def shuffle_password(password: str):
    psw = list(password)
    shuffle(psw)
    return ''.join(psw)

def add_numbers_to_password(n: int):
    nums = ''
    for i in range(n):
        nums += choice(digits)
    
    return nums
    

def add_special_characters_to_password(sc: int):
    specials = ''
    punctuation = "!?=+-()#"

    for i in range(sc):
        specials += choice(punctuation)
    
    return specials

def generate_strong_password(length: int, numbers: bool, special_character: bool):
    password = ''

    if numbers:
        n = randint(1, length//2)
        password += add_numbers_to_password(n)
        length -= n
    
    if special_character:
        sc = randint(1, length//2)
        password += add_special_characters_to_password(sc)
        length -= sc

    for i in range(length):
        password += choice(ascii_lowercase)
    
    
    return shuffle_password(password)


if __name__ == "__main__":
    
    for i in range(5):
        print(generate_strong_password(6, True, True))