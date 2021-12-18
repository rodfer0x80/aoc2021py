
# subroutines


# main
def solve_part1(input_ls: list) -> int:
    n: int = 0
    t = input_ls[0]
    input_ls = input_ls[2:]
    xs = list()
    for x in input_ls:
        xs.append(list(x.split(" -> ")))    
        
    print(t,xs)


    return n

def solve_part2(input_ls: list) -> int:
    return 0


def solve_day14(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

