 # Write your solution here
def factorials(n: int):
    numbers = {}
    num = 1
    
    for i in range(1, n + 1):
        num *= i
        numbers[i] = num

    return numbers

if __name__ == "__main__":
   k = factorials(5)
   print(k[1])
   print(k[3])
   print(k[5]) 

   