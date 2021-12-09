def solve_part1(input_ls: list) -> int:
    score = 0
    bingo = list(x for x in input_ls[0] if x != ',' and x != ' ')
    _boards = list(board for board in input_ls[2:])
    boards = list()
    new_board = list()

    for line in _boards:
        if line != "":
            new_board.append(line)
        else:
            _boards.append(new_board)
            new_board = list()

    for board in _boards:
        win_cases = dict()
        for line in board:
            for num in line.split():
                win_cases[num] = False
            boards.append(win_cases)

    for num in bingo:
        for board in boards:
            print(board)
            for win_cases in board:
                continue
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
