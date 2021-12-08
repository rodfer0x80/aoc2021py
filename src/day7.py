from functools import lru_cache


def get_simple_pos(input_ls: list) -> list:
    pos = []
    for el in input_ls:
        pushed = False
        for i in pos:
            if el == i[0]:
                i[1] += 1
                pushed = True
        if pushed == False:
            pos.append([el, 1])
            pushed = False
    return pos

def move1(x: int, y: int) -> int:
    return abs(x-y)

@lru_cache(maxsize=1024)
def move2(x: int, y: int) -> int:
    cost = 0
    c = abs(x-y)
    for i in range(1, c+1):
        cost += i
    return cost

def find_min_pos(xs: list) -> int:
    min_v = xs[0][0]
    for i in xs:
        if min_v > i[0]:
            min_v = i[0]
    return min_v

def find_max_pos(xs: list) -> int:
    max_v = xs[0][0]
    for i in xs:
        if max_v < i[0]:
            max_v < i[0]
    return max_v

def calculate_moves(pos: list, part: int) -> int:
    if part == 1:
        move = move1
    if part == 2:
        move = move2
    min_pos = find_min_pos(pos)
    max_pos = find_max_pos(pos)
    cost = 0
    for i in range(min_pos, max_pos):
        total = 0
        for el in pos:
            total += el[1] * move(el[0], i)
        if cost == 0 or cost > total:
            cost = total
    return cost


def solve_part1(input_ls: list) -> int:
    pos = get_simple_pos(input_ls)
    fuel = calculate_moves(pos, 1)
    return fuel
    

def solve_part2(input_ls: list) -> int:
    pos = get_simple_pos(input_ls)
    fuel = calculate_moves(pos, 2)
    return fuel


def solve_day7(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output
