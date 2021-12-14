#!/usr/bin/python3
from sys import argv, stderr, exit
from os import system
from os.path import isdir

def new_day(type: str, day: str) -> int:
    with open("__main__.py", 'r') as fp:
        main = fp.read().split('\n')
    new_main = ""
    i = 0
    banish = 0
    for line in main:
        if line.strip() == f"from src.day{day-1} import solve_day{day-1}":
            line = f"from src.day{day-1} import solve_day{day-1}\nfrom src.day{day} import solve_day{day}"
        if line.strip() == f"elif day == {day-1}:":
            new_entry = f'    elif day == {day}:\n        utils.read_input("str")\n        output = solve_day{day}(utils.input_arr)'
            line = f"{line}\n{main[i+1]}\n{main[i+2]}\n{new_entry}"
            banish = 3
            new_main += f"{line}\n"
        i += 1
        if banish == 0:
            new_main += f"{line}\n"
        else:
            banish -= 1
    with open("__main__.py", 'w') as fp:
        fp.write(new_main)

    with open("src/day0.py", 'r') as fp:
        day_code = fp.read().split('\n')
    new_day_code = ""
    for line in day_code:
        if line.strip() == "def solve_day0(input_ls: list) -> list:":
            line = f"def solve_day{day}(input_ls: list) -> list:"
        new_day_code += f"{line}\n"
    with open(f"src/day{day}.py", 'w') as fp:
        fp.write(new_day_code)

    if isdir("inputs"):
        system(f"touch inputs/day{day}-input.txt")
    return 0


def reborn(day: str) -> int:
    with open(argv[0], 'r') as fp:
        code = fp.read().split('\n')
    code_reborn = ""
    for line in code:
        if line.strip() == f"day = {day}":
            line = f"    day = {day+1}"
        code_reborn += f"{line}\n"
    with open(argv[0], 'w') as fp:
        fp.write(code_reborn)

    return 0


if __name__ == '__main__':
    day = 15

    if len(argv) != 2:
        stderr.write(f"Usage: {argv[0]} <input_type>\ninput_types: csv/int, csv/str, int, str\n")
        exit(0)

    if new_day(argv[1], day) != 0:
        stderr.write(f"Fatal error initialising new day {day}\n")
        exit(0)

    if reborn(day) == 0:
        print(f"Successfully initialised day {day} with {argv[1]} input")
        exit(0)
    else:
        stderr.write(f"Fatal error during script code rewriting\n")
        exit(0)








