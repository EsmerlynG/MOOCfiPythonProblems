# Write your solution here
def store_personal_data(person: tuple):
    line = ''
    for data in person:
        line += (str(data) + ';')
    line = line[:-1]

    
    with open("people.csv", "a") as my_file:
        my_file.write(f"{line}\n")

        


if __name__ == "__main__":
    person = ('vilatro', 14, 199.65)
    store_personal_data(person)
    person = ('bob', 65, 123.65)
    store_personal_data(person)
    person = ('mile', 34, 199.65)
    store_personal_data(person)