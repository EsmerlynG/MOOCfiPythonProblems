# Write your solution here
from datetime import datetime
def calculate_age(day: int, month: int, year: int) -> int:
    millenium = datetime(1999, 12, 31)
    birthday = datetime(year, month, day)
    difference = millenium - birthday

    return difference.days


Day = int(input("Day: "))
Month = int(input("Month: "))
Year = int(input("Year: "))
age = calculate_age(Day, Month, Year)
    
if age < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {age} days old on the eve of the new millennium.")
