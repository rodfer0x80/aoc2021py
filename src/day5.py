import collections


def format_vents(input_ls: list) -> list:
    return list(vent.split(" -> ") for vent in input_ls)


def cordinate(obj):
    # Convert the co-ordinates from string format to int format
    return tuple(map(int, obj.split(',')))


def draw_horizontal_line(grid, y, x, x1):
    intersections = 0
    # Range is inclusive of both ends i.e., min to max
    for i in range(min(x, x1), max(x, x1) + 1):
        grid[(i, y)] += 1
        
        # Once we find a intersection, we increment the intersections counter
        if grid[(i, y)] == 2:
            intersections += 1
    return intersections


def draw_vertical_line(grid, x, y, y1):
    intersections = 0
    # Range is inclusive of both ends i.e., min to max
    for i in range(min(y, y1), max(y, y1) + 1):
        grid[(x, i)] += 1

        # Once we find a intersection, we increment the intersections counter
        if grid[(x, i)] == 2:
            intersections += 1
    return intersections


def solve_part2(input_ls: list) -> int:
    lines = format_vents(input_ls)

    return 0


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


def solve_day5(input_ls: list) -> list:
    output = list()

    part1 = solve_part1(input_ls)
    output.append(part1)

    part2 = solve_part2(input_ls)
    output.append(part2)

    return output

