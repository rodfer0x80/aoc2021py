# imports


# subroutines

def calculate_flashes(i, r, xs):
    sx = len(xs)
    c = 0
    if xs[i] > 9:
        xs[i] = 0
        c += 1
        if i+1 < sx:
            xs[i+1] = xs[i+1] + 1
        if i-1 > -1:
            xs[i-1] = xs[i-1] + 1

        if i+r < sx:
            xs[i+r] = xs[i+r] + 1
        if i-r > -1:
            xs[i-r] = xs[i-r] + 1

        if i+r+1 < sx:
            xs[i+r+1] = xs[i+r+1] + 1
        if i-r+1 > -1:
            xs[i-r+1] = xs[i-r+1] + 1

        if i-r-1 > -1:
            xs[i-r-1] = xs[i-r-1] + 1
        if i+r-1 < sx:
            xs[i+r-1] =  xs[i+r-1] + 1
    return xs, c

# main
def solve_part1(input_ls: list) -> int:
    r = 10
    f = 0
    xs = list()
    for line in input_ls:
        for char in line:
            xs.append(int(char))
    for _ in range(100):
        for i in range(len(xs)):
            xs[i] += 1
            xs, c = calculate_flashes(i, r, xs)
            f += c
    return f


def solve_part2(input_ls: list) -> int:
    return 0


def solve_day11(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

