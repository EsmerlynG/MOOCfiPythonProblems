# Write your solution here
def create_set_of_words():
    word_set = set()
    with open("words.txt", "r") as wf:
        for line in wf:
            word_set.add(line.strip())

    return word_set

def astriks_in_term(term: str, words_set: set):
    matched_words = []
    if term.startswith("*"):
        for word in words_set:
            if word.endswith(term[1:]):
                matched_words.append(word)

    elif term.endswith("*"):
        for word in words_set:
            if word.startswith(term[:-1]):
                matched_words.append(word)

    return sorted(matched_words)

def period_in_term(term: str, words_set: set):
    matched_words = []
    
    for word in words_set:
        same = True
        for i in range(len(word)):
            if term[i] != '.' and word[i] != term[i]:
                same = False
                break

        if same:
            matched_words.append(word) 
        
    return sorted(matched_words)


def find_words(term: str, words_set: set):
    matched_words = []

    if "*" in term:
        return astriks_in_term(term, words_set)
    
    elif "." in term: 
        same_length_words = {word for word in words_set if len(word) == len(term)}   
        return period_in_term(term, same_length_words)

    elif term in words_set:
        matched_words.append(term)
        
    return matched_words



if __name__ == "__main__":
    words_set = create_set_of_words()
    print(find_words("ca.", words_set))
    """To pass tests remove words_set as a parameter
       and instead make it a variable in find_words()"""
   
