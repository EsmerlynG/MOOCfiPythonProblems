# Write your solution here
from difflib import get_close_matches

def autocorrect(string: str) -> tuple[str, dict[str, list[str]]]:
    parts = string.strip().split()
    incorrect_words = {}

    with open("wordlist.txt", "r") as wf:
        wordslist = set(word.strip() for word in wf)
    
    for index, word in enumerate(parts):
        if word.lower() not in wordslist:
            incorrect_words[word] = get_close_matches(word, wordslist)
            parts[index] = f"*{word}*"
    
    return " ".join(parts), incorrect_words
    

def main():
    string = input("Write text: ")
    sentence, incorrect_words = autocorrect(string)
    print(sentence)
    print("suggestions: ")
    for word, suggestions in incorrect_words.items():
        print(f'{word}: {", ".join(suggestions)}')

main()