# Write your solution here
name = input("Whom should I sign this to: ")
txt_file = input("Where shall I save it: ")

with open(txt_file, "w") as f:
    f.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

with open(txt_file, "r") as f:
    for line in f:
        print(line.strip())