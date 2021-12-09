
def solve_part1(input_ls: list) -> int:
    counter = 0
    for i in range(len(input_ls)):
        # check if its a boarder 
        if i % len(input_ls[0]) == 0:
            if input_ls[i] <= input_ls[i+1] and \
                    input_ls[i] <= input_ls[i-1] and \
                        input_ls[i] <= input_ls[i+len(input_ls[0])]:
                counter += 1
                
        elif i-1+len(input_ls[0]) % len(input_ls[0]) == 0:
            if 
        elif i<len(input_ls[0]):

        elif len(input_ls)-i<len(input_ls[0]):

        elif input_ls[i] <= input_ls[i+1] and \
                input_ls[i] <= input_ls[i-1] and \
                    input_ls[i] <= input_ls[i+len(input_ls[0])] and \
                        input_ls[i] <= input_ls[i-len(input_ls[0])]:
            counter += 1
    return counter
    

def solve_part2(input_ls: list) -> int:
    return 0


def solve_day9(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output
