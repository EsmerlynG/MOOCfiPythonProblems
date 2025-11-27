# Write your solution here
def tens_list(tens: list, ones: list):
    string_num = []

    for numbers in tens:
        string_num.append(numbers)
        for num in range(len(ones)):
            tens_num = numbers + "-" + ones[num]
            string_num.append(tens_num)

    return string_num


def complete_numbers_list():
    complete_list = ["zero"]

    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    complete_tens = tens_list(tens, ones)

    complete_list += ones[:]
    complete_list += teens[:]
    complete_list += complete_tens[:]

    return complete_list



def dict_of_numbers():
    dictionary = {}
    
    complete_list = complete_numbers_list()

    for num in range(100):
        dictionary[num] = complete_list[num]
    
    return dictionary


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[5])
    