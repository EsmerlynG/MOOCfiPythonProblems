# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False
    
    for num in pic[:6] + pic[7:10]:
        if num not in "0123456789":
            return False
    
    if pic[6] not in "-+A":
        return False
    
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    century_marker = pic[6]
    iden = pic.split(century_marker)
    birthday = iden[0]
    id_num = iden[1]
    special_char_index = int(iden[0] + iden[1][:3]) % 31
    
    day = int(birthday[0:2])
    month = int(birthday[2:4])
    year = 0

    if century_marker == "+":
        year = int("18" + birthday[4:])
    elif century_marker == "-":
        year = int("19" + birthday[4:])

    elif century_marker == "A":
        year = int("20" + birthday[4:])

    try: 
        datetime(year, month, day)
    
    except ValueError:
        return False
    
    
    return characters[special_char_index] == id_num[-1]
    
    
if __name__ == "__main__":
    pic = ("310823A9877")
    print(is_it_valid(pic))
