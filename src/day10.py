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
    

def autocomplete_uncorrupted_lines(input_ls: list) -> int:
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    bracket_mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    total_scores = list()

    for line in input_ls:
        is_corrupt = False
        stack = []
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
                is_corrupt = True
                break
        if is_corrupt:
            continue
        score = 0
        stack.reverse()
        for char in stack:
            score = score * 5 + points[bracket_mapping[char]]
        total_scores.append(score)

    total_scores.sort()
    return total_scores[len(total_scores) // 2]


def solve_part2(input_ls: list) -> int:
    score = autocomplete_uncorrupted_lines(input_ls)
    
    return score


def solve_day10(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output

