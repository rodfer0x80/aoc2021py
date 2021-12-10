def solve_part1(input_ls: list) -> int:
    score = 0
    bingo = list(x for x in input_ls[0] if x != ',' and x != ' ')
    boards2 = list(board for board in input_ls[2:])
    boards1 = list()
    boards = list()
    new_board = list()
    
    for line in boards2:
        if line != "":
            new_board.append(line)
        else:
            print(new_board)
            boards1.append(new_board)
            new_board = list()

    for board in boards1:
        new_board = list()
        for line in board:
            line = line.split()
            win_cases = dict()
            for num in line:
                win_cases[num] = False
            new_board.append(win_cases)
        boards.append(new_board)

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
