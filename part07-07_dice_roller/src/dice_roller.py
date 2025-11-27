# Write your solution here
from random import choice

def choose_dice(die: str):
    dice = ()
    if die == "A":
        dice = (3,3,3,3,3,6)
    elif die == "B":
        dice = (2,2,2,5,5,5)
    elif die == "C":
        dice = (1,4,4,4,4,4)
    return dice

def roll(die: str):
    return choice(choose_dice(die))

def play(die1: str, die2: str, times: int):
    d1 = 0
    d2 = 0
    tie = 0
    for i in range(times):
        if roll(die1) == roll(die2):
            tie += 1
        elif roll(die1) > roll(die2):
            d1 += 1
        else:
            d2 += 1

    
    return (d1, d2, tie)

if __name__ == "__main__":
    result = play("C", "C", 1000)
    print(result)

    
