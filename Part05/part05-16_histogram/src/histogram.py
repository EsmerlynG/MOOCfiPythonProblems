# Write your solution here
def create_stats(word: str):
    groups = {}

    for letter in word:
        
        if letter not in groups:
            groups[letter] = []
    
        groups[letter].append("*")

    return groups

def histogram(word: str):
    groups = create_stats(word)

    for key, value in groups.items():
        print(f"{key} ", end="")
        for stats in value:
            print(f"{stats}", end="")
        print()

    
if __name__ == "__main__":
    histogram("statistically")
    