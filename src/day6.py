def solve_part1(xs: list) -> int:
    # bruteforce :: everyday update array and append newborns 
    for i in range(80):
        i = 0
        for x in xs:
            xs[i] = x - 1
            i += 1
        i = 0
        for x in xs:
            if x == -1:
                xs[i] = 6
                xs.append(8)
            i += 1
    return len(xs)


def solve_part2(input_arr: list) -> int:
    # scientific method :: make an array for each day of the cycle
    # and manage the number of fishes in each day of the cycle for each 9 day
    # thus counting the newborns for each cycle
    days = [0] * 9
    for fish in input_arr:
        days[fish] += 1
    for i in range(256):
        today = i % len(days) 
        days[(today + 7) % len(days)] += days[today]
    return sum(days)


def solve_day6(input_arr: list) -> list:
    output = []
    part1 = solve_part1(input_arr)
    output.append(part1)
    part2 = solve_part2(input_arr)
    output.append(part2)
    return output
