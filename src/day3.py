def binary_count(bin):
    n = 0
    for i in bin:
        n += 1
    return 2**n

def digit_count(num):
    n = 0
    for i in num:
        n += 1
    return n

def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def solve_part1(input_arr: list) -> int:
    gamma = ""
    epsilon = ""
    size_arr = len(input_arr)
    size_bin = len(input_arr[0])
    counters = []
    for i in range(size_bin):
        counters.append(0)

    for bin_str in input_arr:
        for i in range(size_bin):
            counters[i] += int(bin_str[i])
    for i in range(size_bin):
        if size_arr-counters[i] <= counters[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    epsilon_bin = epsilon
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma*epsilon, epsilon_bin
            


def solve_part2(input_arr: list, epsilon: str) -> int:
    oxygen = ""
    carbon = "10"
    i = 0
    sol_arr = input_arr
    for digit in epsilon:
        for number in sol_arr:
            if str(number[i]) != digit:
                sol_arr.remove(number)
        i += 1
    
    print(sol_arr)
    oxygen = sol_arr[0]
    oxygen = int(oxygen, 2)
    carbon = int(carbon, 2)
    return oxygen*carbon


def solve_day3(input_arr: list) -> list:
    output = []
    part1, epsilon = solve_part1(input_arr)
    output.append(part1)
    part2 = solve_part2(input_arr, epsilon)
    output.append(part2)
    return output