# Write your solution here
def new_person(name: str, age: int):
    if len(name.split()) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("Invalid value or values")
    
    return (name, age)

if __name__ == "__main__":
    
    name = input("Please enter a name: ")
    age = int(input("Please enter a age: "))
    print(new_person(name, age))