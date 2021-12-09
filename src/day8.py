from functools import lru_cache


def format__list(xs: list, delim: str) -> list:
    return list(list(x.split(delim))for x in xs)


@lru_cache(maxsize=256)
def decode_pattern(digit: str) -> int:
    if len(digit) == 2:
        return 1
    elif len(digit) == 4:
        return 4
    elif len(digit) == 3:
        return 7
    elif len(digit) == 7:
        return 8
    else:
        return -1

# @lru_cache(maxsize=256)
# def decode_pattern(digit: str) -> int:
#     if len(digit) == 2:
#         return 1
#     elif len(digit) == 4:
#         return 4
#     elif len(digit) == 3:
#         return 7
#     elif len(digit) == 7:
#         return 8
#     else:
#         return digit


@lru_cache(maxsize=256)
def deduce_pattern(digits: str, patterns: list) -> int:
    decoded_patterns = []
    for pattern in patterns.split(" "):
        decoded_digit = decode_pattern(pattern)
        if decoded_digit != -1:
            decoded_patterns.append([decoded_digit, pattern])
    decoded_patterns = sorted(decoded_patterns)
    one = decoded_patterns[0][1]
    four = decoded_patterns[1][1]
    seven = decoded_patterns[2][1]
    eight = decoded_patterns[3][1]

    # find a
    a = seven
    for digit in decoded_patterns[0][1]:
        a = a.replace(digit, '')

    # find c and f
    cf = one
    c = cf[:1]
    f = cf[1:]
    six = eight.replace(c, '')
    if len(six) == len(eight):
        tmp = f
        f = c
        c = tmp
        six = eight.replace(f, '')
    # find d
    arr = []
    for pattern in patterns.split(" "):
        if len(pattern) == 6:
            arr.append(pattern)
    zero  = arr[0]
    nine = arr[2]
    d = nine
    for digit in zero:
        d = d.replace(digit, '')
    # find e
    e = eight
    for digit in nine:
        e = e.replace(digit, '')

    # find b
    b = four
    b = b.replace(d, '')
    b = b.replace(f, '')
    b = b.replace(c, '')
    print(b)
    # from this point we have a,c,d,e,f



    return 0


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
    xs = format__list(input_ls, " | ")
    patterns = list()
    digits = list()
    total = 0
    for x in xs:
        patterns.append(x[0])
        digits.append(x[1])
    for i in range(len(digits)):
        n = deduce_pattern(digits[i], patterns[i])
        total += n
    return total


def solve_day8(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

