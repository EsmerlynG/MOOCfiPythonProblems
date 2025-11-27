# Write your solution here
from fractions import *

def fractionate(ammount: int):
    n = []
    
    for i in range(ammount):
        n.append(Fraction(1, ammount))
    
    return n



if __name__ == "__main__":

    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(3))
