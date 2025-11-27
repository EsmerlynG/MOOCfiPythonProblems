# Write your solution here
def read_input(string: str, start: int, end: int):

    while True:
        try:
            input_string = input(string)
            num = int(input_string)
            if start < num < end:
                return num
            
        except ValueError:
            pass

        print(f"You must type in an integer between {start} and {end}")

if __name__ == "__main__":
    
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
