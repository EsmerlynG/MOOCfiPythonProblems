# Write your solution here
from random import sample
def words(n: int, beginning: str) -> list[str]:

    with open("words.txt", "r") as word_file:
        matched_words = [line.strip() for line in word_file if line.strip().startswith(beginning)]

    if len(matched_words) < n:
        raise ValueError(f"Not enough matching words found. Found {len(matched_words)}, needed {n}")
    
    return sample(matched_words, n)
    

if __name__ == "__main__":
    words_set = words(5, "abs")
    for word in words_set:
        print(word)