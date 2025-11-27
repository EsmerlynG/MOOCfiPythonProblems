# Write your solution here
def create_tuple(x: int, y: int, z: int):
    numbers = (x, y, z)
    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)
    
    return (smallest, largest, total)


if __name__ == "__main__":
    print(create_tuple(1, 4, 7))