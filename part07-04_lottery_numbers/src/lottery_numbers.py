# Write your solution here
from random import sample

def lottery_numbers(ammount: int, lower: int, upper: int):
    return sorted(sample(list(range(lower, upper + 1)), ammount))
    


if __name__ == "__main__":

    for number in lottery_numbers(7, 1, 40):
        print(number)
