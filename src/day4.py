




def solve_part1(input_ls: list) -> int:
    score = 0
    bingo = list(input_ls[0].split(" "))
    _boards = input_ls[2:]
    boards = list()
    for board in _boards.split("\n\n"):
        win_cases = dict()
        for num in board.split(" "):
            win_cases[num] = False
        boards.append(win_cases)
    print(bingo)
    # for num in bingo:
    #     for board in boards:
    #         for win_case in board:
    #             if num in win_case.keys():
    #                 win_case[num] = True
    #             state = True
    #             for s in win_case.values():
    #                 if s == False:
    #                     state = s
    #             if state == True:
    #                 for num in win_case.keys():
    #                     score += num

    return score
    

def solve_part2(input_ls: list) -> int:
    return 0


def solve_day4(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output
