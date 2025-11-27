# Write your solution here
print("1 - add an entry, 2 - read entries, 0 - quit: ")

while True:
    function = int(input("Function: "))

    if function == 0:
        break

    elif function == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as af:
            af.write(entry + "\n")
            print("Diary saved")

                
    elif function == 2:
        print("Entries: ")
        with open("diary.txt", "r") as rf:
            for line in rf:
                print(line.strip())

        
print("Bye now")