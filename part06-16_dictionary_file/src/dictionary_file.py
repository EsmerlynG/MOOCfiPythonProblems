def get_def_from_dict(term):

    with open("dictionary.txt", "r") as dict_file:
        for line in dict_file:
            parts = line.strip().split()

            for word in parts:
                if term == '-':
                    continue
                elif term.lower() in word.lower():
                    print(line.strip())

def add_to_dict(fin_word: str, eng_word: str):
    
    with open("dictionary.txt", "a") as dict_file:
        line = f"{fin_word} - {eng_word}\n"
        dict_file.write(line)

def main():

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        choice = int(input("Function: "))

        if choice == 3:
            print("Bye!")
            break
        elif choice == 1:
            fin = input("The word in Finnish: ")
            eng = input("The word in English: ")
            add_to_dict(fin, eng)
            print("Dictionary entry added")
        elif choice == 2:
            term = input("Search term: ")
            get_def_from_dict(term)
        else: 
            print("Enter a number 1 - 3 please.")
    

main()