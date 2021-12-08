def solve_part1(input_ls: list) -> int:
    depth = 0
    horizontal = 0
    for action in input_ls:
        move, distance = action.split(" ")
        distance = int(distance)
        if move == "forward":
            horizontal += distance
        elif move == "up":
            depth -= distance
        elif move == "down":
            depth += distance
    return depth*horizontal


def solve_part2(input_ls: list) -> int:
    depth = 0
    horizontal = 0
    aim = 0
    for action in input_ls:
        move, distance = action.split(" ")
        distance = int(distance)
        if move == "forward":
            horizontal += distance
            depth += distance*aim
        elif move == "up":
            aim -= distance
        elif move == "down":
            aim += distance
    return depth*horizontal



def solve_day2(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output