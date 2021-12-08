def solve_part1(input_ls: list) -> int:
    increases = 0
    for i in range(len(input_ls)):
        if i == 0:
            continue
        elif input_ls[i] > input_ls[i - 1]:
            increases += 1
    return increases


def solve_part2(input_ls: list) -> int:
    increases = 0
    previous_sum = 0
    current_sum = 0
    for i in range(len(input_ls) - 1):
        if i == 0:
            continue
        previous_sum = current_sum
        current_sum = input_ls[i - 1] + input_ls[i] + input_ls[i + 1]
        if previous_sum != 0 and current_sum > previous_sum:
            increases += 1
    return increases


def solve_day1(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

