# Write your solution here

def add(people: dict, name: str, phone_num: str):
    people[name] = phone_num

def search(people: dict, name: str):
    if name in people:
        return people[name]
        
    return "no number"

def phone_book():
    people = {}

    while True:
        command = input("Command (1 search, 2 add, 3 quit): ")

        if command == "1":
            name = input("Name: ")
            name = name.lower()
            print(search(people, name))

        elif command == "2":
            name = input("Name: ")
            phone_num = input("Phone: ")
            add(people, name, phone_num)
            print("ok!")
        else:
            break
    
    print("quitting...")

phone_book()


