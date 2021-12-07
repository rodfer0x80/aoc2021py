from sys import stdout


def solve_part1(input_arr: list) -> int:
    fishpool: list = input_arr
    new_fishpool:list
    newborn_fishpool: list
    for i in range(80):
        new_fishpool = []
        newborn_fishpool = []
        # print(f"Day: {i+1}")
        # stdout.flush()
        for fish in fishpool:
            fish -= 1
            if fish == -1:
                fish = 6
                newfish = 8
                newborn_fishpool.append(newfish)
            new_fishpool.append(fish)
        fishpool = new_fishpool + newborn_fishpool
    return len(fishpool)

        
def solve_part2(input_arr: list) -> int:
    return 0


def solve_day6(input_arr: list) -> list:
    imparr = [3,4,3,1,2]
    print(solve_part1(imparr))
    output = []
    part1 = solve_part1(input_arr)
    output.append(part1)
    part2 = solve_part2(input_arr)
    output.append(part2)
    return output
