# Write your solution here
from string import ascii_uppercase


def print_to_list(dictionary: dict, results_list: list, variable: str) -> None:
    if variable in ascii_uppercase:
        results_list.append(dictionary[variable])
    else: 
        results_list.append(int(variable))
    
def mov(dictionary: dict, variable: str, value: str|int) -> None:
    """ Assigns the value to the variable """
    if str(value) not in ascii_uppercase:
        dictionary[variable] = int(value)
    else:
        dictionary[variable] = dictionary[value]

    """Add, Substract or multiply varibales"""
def add(dictionary: dict, variable: str, value: int|str) -> None:
    if str(value) in ascii_uppercase:
        dictionary[variable] += dictionary[value]
    else:
        dictionary[variable] += int(value)

def sub(dictionary: dict, variable: str, value: int|str) -> None:
    if str(value) in ascii_uppercase:
        dictionary[variable] -= dictionary[value]
    else:
        dictionary[variable] -= int(value)
    
def mul(dictionary: dict, variable: str, value: int|str) -> None:
    if str(value) in ascii_uppercase:
        dictionary[variable] *= dictionary[value]
    else:
        dictionary[variable] *= int(value)


    
def jump(program: list, location: str) -> int:
    """ go to the specified location in the program list """
    label = location if location.endswith(":") else location + ":"
    return program.index(label)

    
def condition(dictionary: dict, variable1: str, variable2: str, con: str) -> bool:
    """ execute specific operation based on conditional statement """
    if variable1 in ascii_uppercase:
        val1 = dictionary[variable1]
    else:
        val1 = int(variable1)
    
    if variable2 in ascii_uppercase:
        val2 = dictionary[variable2]
    else:
        val2 = int(variable2)
    
    
    if con == "==":
        return val1 == val2
    if con == "!=":
        return val1 != val2
    if con == "<=":
        return val1 <= val2
    if con == ">=":
        return val1 >= val2
    if con == ">":
        return val1 > val2
    if con == "<":
        return val1 < val2
    
    return False




def run(program: list) -> list[int]:
    result_list = []
    variables = {letter: 0 for letter in ascii_uppercase}
    """adds letters A-Z into the dict and assigns all of them a value of 0"""
    index = 0
 
    dispatch = {
        "PRINT": lambda parts: print_to_list(variables,result_list, parts[-1]),
        "MOV":   lambda parts: mov(variables, parts[1], parts[-1]),
        "ADD":   lambda parts: add(variables, parts[1], parts[-1]),
        "SUB":   lambda parts: sub(variables, parts[1], parts[-1]),
        "MUL":   lambda parts: mul(variables, parts[1], parts[-1]),
        "JUMP":  lambda parts: jump(program, parts[-1]),
        "IF":    lambda parts: condition(variables, parts[1], parts[3], parts[2])
    }

    while index < len(program):
        parts = program[index].strip().split()
        command = parts[0]

        if command in dispatch:
            result = dispatch[command](parts)
            #handle JUMP, END and IF
            if command == "END":
                break

            if command == "JUMP":
                index = result
                continue
            
            if command == "IF":
                if result:
                    index = dispatch["JUMP"](parts)
                    continue
        
        index += 1

    return result_list



if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)

