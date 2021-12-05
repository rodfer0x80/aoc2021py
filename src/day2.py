from sys import stderr, exit


def solve_part1(input_arr: list) -> int:
    depth = 0
    horizontal = 0
    for action in input_arr:
        move, distance = action.split(" ")
        distance = int(distance)
        if move == "forward":
            horizontal += distance
        elif move == "up":
            depth -= distance
        elif move == "down":
            depth += distance
        else:
            stderr.write("[!] Error listening to command")
            exit(0)
    return depth*horizontal


def solve_part2(input_arr: list) -> int:
    depth = 0
    horizontal = 0
    aim = 0
    for action in input_arr:
        move, distance = action.split(" ")
        distance = int(distance)
        if move == "forward":
            horizontal += distance
            depth += distance*aim
        elif move == "up":
            aim -= distance
        elif move == "down":
            aim += distance
        else:
            stderr.write("[!] Error listening to command")
            exit(0)


    return depth*horizontal



def solve_day2(input_arr: list) -> list:
    output = []
    part1 = solve_part1(input_arr)
    output.append(part1)
    part2 = solve_part2(input_arr)
    output.append(part2)
    return output