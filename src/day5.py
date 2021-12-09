import collections


def format_vents(input_ls: list) -> list:
    return list(vent.split(" -> ") for vent in input_ls)


def cordinate(obj: str) -> int:
    return tuple(map(int, obj.split(',')))


def draw_horizontal_line(grid: dict, y: int, x: int, x1: int) -> int:
    intersections = 0
    for i in range(min(x, x1), max(x, x1) + 1):
        grid[(i, y)] += 1      
        if grid[(i, y)] == 2:
            intersections += 1
    return intersections


def draw_vertical_line(grid: dict, x: int, y: int, y1: int) -> int:
    intersections = 0
    for i in range(min(y, y1), max(y, y1) + 1):
        grid[(x, i)] += 1
        if grid[(x, i)] == 2:
            intersections += 1
    return intersections


def draw_diagonal_line(grid: dict, x: int, y: int, x1: int, y1: int) -> int:
    counter = 0
    upto = abs(x1 - x)
    for _ in range(upto + 1):
        grid[(x, y)] += 1
        if grid[(x, y)] == 2:
            counter += 1
        x += 1 if x1 > x else -1
        y += 1 if y1 > y else -1
    return counter


def solve_part1(input_ls: list) -> int:
    lines = format_vents(input_ls)
    grid = collections.defaultdict(int)
    counter = 0
    
    for line in lines:
        p1, p2 = tuple(map(cordinate, line))
        if p1[0] == p2[0]:
            counter += draw_vertical_line(grid, p1[0], p1[1], p2[1])
        elif p1[1] == p2[1]:
            counter += draw_horizontal_line(grid, p1[1], p1[0], p2[0])

    return counter


def solve_part2(input_ls: list) -> int:
    lines = format_vents(input_ls)
    grid = collections.defaultdict(int)
    counter = 0

    for line in lines:
        p1, p2 = tuple(map(cordinate, line))
        if p1[0] == p2[0]:
            counter += draw_vertical_line(grid, p1[0], p1[1], p2[1])
        elif p1[1] == p2[1]:
            counter += draw_horizontal_line(grid, p1[1], p1[0], p2[0])
        else:
            counter += draw_diagonal_line(grid, p1[0], p1[1], p2[0], p2[1])
            
    return counter

    
def solve_day5(input_ls: list) -> list:
    output = list()

    part1 = solve_part1(input_ls)
    output.append(part1)

    part2 = solve_part2(input_ls)
    output.append(part2)

    return output

