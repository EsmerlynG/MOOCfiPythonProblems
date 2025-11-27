# Write your solution here
def double_items(numbers: list):
    new_list = numbers[:]
    for i in range(len(numbers)):
        new_list[i] *= 2
    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    print(double_items(numbers))