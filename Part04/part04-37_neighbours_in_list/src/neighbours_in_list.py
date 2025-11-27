# Write your solution here
def longest_series_of_neighbours(my_list):
    longest_series = []
    series = []
    pair = my_list[0]
    my_list = my_list[1:]
    my_list.append(my_list[-1] + 2)

    for num in my_list:
        if pair - num == 1 or num - pair == 1:
            series.append(pair)
        else:
            if len(longest_series) <= len(series):
                series.append(pair)
                longest_series = series
            series = []
        pair = num

    return len(longest_series)

if __name__ == "__main__":
    my_list = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
    print(longest_series_of_neighbours(my_list))