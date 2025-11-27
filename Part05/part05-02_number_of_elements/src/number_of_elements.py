# Write your solution here
# define count matching elements function
def count_matching_elements(my_matrix: list, searched_number: int):
    count = 0
    for row in my_matrix:
        count += row.count(searched_number)

    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))  