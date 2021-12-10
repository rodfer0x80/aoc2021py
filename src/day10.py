def scan_illegal_chars(input_ls: list) -> list:
    illegal_chars = list()
    for line in input_ls:
        stack = list()
        for char in line:
            gt = char == '>' and len(stack) > 0 and stack[-1] == '<'
            sq = char == ']' and len(stack) > 0 and stack[-1] == '['
            cl = char == '}' and len(stack) > 0 and stack[-1] == '{'
            ci = char == ')' and len(stack) > 0 and stack[-1] == '('
            if gt or sq or cl or ci:
                stack.pop()
            elif char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                illegal_chars.append(char)
                break
    return illegal_chars

def solve_part1(input_ls: list) -> int:
    illegal_chars = scan_illegal_chars(input_ls)
    illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    }
    score = sum([illegal_points[char] for char in illegal_chars])
    return score
    
def scan_uncorrupted_lines(input_ls: list) -> list:
    illegal_chars = list()
    uncorrupted_lines = input_ls
    i = 0
    for line in input_ls:
        stack = list()
        for char in line:
            gt = char == '>' and len(stack) > 0 and stack[-1] == '<'
            sq = char == ']' and len(stack) > 0 and stack[-1] == '['
            cl = char == '}' and len(stack) > 0 and stack[-1] == '{'
            ci = char == ')' and len(stack) > 0 and stack[-1] == '('
            if gt or sq or cl or ci:
                stack.pop()
            elif char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                illegal_chars.append(char)
                uncorrupted_lines.pop(i)
                break
        i += 1
    return uncorrupted_lines

def autocomplete(lines: list) -> int:
    score = 0
    for line in lines:
        for sym in line:
            score += 1 
    return score

def solve_part2(input_ls: list) -> int:
    uncorrupted_lines = scan_uncorrupted_lines(input_ls)
    score = autocomplete(uncorrupted_lines)
    return score


def solve_day10(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

