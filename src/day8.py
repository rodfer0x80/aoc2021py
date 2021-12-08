from functools import lru_cache


def format__list(xs: list, delim: str) -> list:
    return list(list(x.split(delim))for x in xs)


@lru_cache(maxsize=256)
def decode_pattern(digit: str) -> int:
    if len(digit) == 2:
        return 1
    if len(digit) == 4:
        return 4
    if len(digit) == 3:
        return 7
    if len(digit) == 7:
        return 8


def count_four_known_digits(xs: list) -> list:
    known_digit = [1, 4, 7, 8]
    c = 0
    for x in xs:
        # pattern = list(x[0].split(" "))
        display = list(x[1].split(" "))
        for digit in display:
            if decode_pattern(digit) in known_digit:
                c += 1
    return c


def solve_part1(input_ls: list) -> int:
    xs = format__list(input_ls, " | ")
    return count_four_known_digits(xs)
    

def solve_part2(input_ls: list) -> int:
    return 0


def solve_day8(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

