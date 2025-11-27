# Write your solution here
def filter_lot_num(lot_num: str):
    num_list = lot_num.split(",")

    try:
        num_list = list(map(int, num_list))

    except ValueError:
        return False
    
    if len(set(num_list)) != 7:
        return False
    
    for num in num_list:
        if num > 39 or num < 1:
            return False
        
    return True


def filter_weeks(week: str):
    parts = week.split()
    week_num = parts[1]

    if len(parts) != 2 or parts[0] != "week":
        return False
    
    try:
        if int(week_num):
            return True
        
    except ValueError:
        return False


def filter_incorrect():
    correct = {}
    try:
        with open("lottery_numbers.csv", "r") as lotNumFile:
            for line in lotNumFile:
                parts = line.strip().split(";")
                week = parts[0]
                lot_num = parts[1]
                
                if filter_weeks(week) and filter_lot_num(lot_num):
                    correct[week] = lot_num
        
    except FileNotFoundError:
        print("Issue reading lottery_numbers.csv")
    
    
    try:
        with open("correct_numbers.csv", "w") as cf:
            for week, lot_num in correct.items():
                cf.write(f"{week};{lot_num}\n")

    except FileNotFoundError:
        print("Problem writing file")
    

if __name__ == "__main__":
    filter_incorrect()

