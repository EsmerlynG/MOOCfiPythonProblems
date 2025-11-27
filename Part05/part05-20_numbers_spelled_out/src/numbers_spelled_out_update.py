# Write your solution here
def dict_of_numbers():
    numbers = {}

    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    for i in range(10):
        numbers[i] = ones[i]

    # handle teens now
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"

    for i in range(2, 10):
        numbers[i * 10] = tens[i]
        for j in range(1, 10):
            numbers[i * 10 + j] = tens[i] + "-" + ones[j]

    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[5])
    print(numbers[12])
    print(numbers[19])
    print(numbers[54])
    print(numbers[96])


    