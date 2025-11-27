# Write your solution here
def invert(s: dict):
    copy = {}

    for key in s:
        copy[key] = s[key]

    for key in copy:
        del s[key]

    for key in copy:
        s[copy[key]] = key
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
