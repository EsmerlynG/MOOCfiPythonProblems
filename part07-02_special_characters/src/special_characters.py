# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(words: str):
    reg_char = ""
    punct = ""
    others = ""
    for char in words:
        if char in ascii_letters:
            reg_char += char
        elif char in punctuation:
            punct += char
        else:
            others += char
    
    return (reg_char, punct, others)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
