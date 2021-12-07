
def get_simple_pos(input_arr: list) -> list:
    pos = []
    for el in input_arr:
        pushed = False
        for i in pos:
            if el == i[0]:
                i[1] += 1
                pushed = True
        if pushed == False:
            pos.append([el, 1])
            pushed = False
    return pos

def move(x: int,y: int) -> int:
    return abs(x-y)

def find_min_pos(arr: list) -> int:
    min_v = arr[0][0]
    for i in arr:
        if min_v > i[0]:
            min_v = i[0]
    return min_v

def find_max_pos(arr: list) -> int:
    max_v = arr[0][0]
    for i in arr:
        if max_v < i[0]:
            max_v < i[0]
    return max_v

def calculate_moves(pos: list) -> int:
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


def solve_part1(input_arr: list) -> int:
    pos = get_simple_pos(input_arr)
    fuel = calculate_moves(pos)
    return fuel
    

def solve_part2(input_arr: list) -> int:
    return 0


def solve_day7(input_arr: list) -> list:
    output = []
    part1 = solve_part1(input_arr)
    output.append(part1)
    part2 = solve_part2(input_arr)
    output.append(part2)
    return output
