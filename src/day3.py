def solve_part1(input_ls: list) -> int:
    gamma = ""
    epsilon = ""
    size_arr = len(input_ls)
    size_bin = len(input_ls[0])
    counters = []
    for i in range(size_bin):
        counters.append(0)

    for bin_str in input_ls:
        for i in range(size_bin):
            counters[i] += int(bin_str[i])
    for i in range(size_bin):
        if size_arr-counters[i] <= counters[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma*epsilon


def solve_part2(input_ls: list) -> int:
    oxygen = ""
    carbon = ""
    oxygen_running = input_ls
    co2_running = input_ls
    total0 = list()
    total1 = list()
    size_e = 0
    for line in input_ls:
        size_e = len(line)
    size_e = len(input_ls[0])
    for i in range(size_e):
        if len(total1) < i + 1:
            total1.append(0)
            total0.append(0)
        for line in oxygen_running:
            char = line[i]
            if char == '1':
                total1[i] = total1[i] + 1
            else:
                total0[i] = total0[i] + 1
        value = "1"
        if total1[i] < total0[i]:
            value = "0"
        oxygen_running = filter_values(oxygen_running, i, value)
        i += 1
    oxygen = list()
    for i in range(len(total1)):
        if total0[i] <= total1[i]:
            oxygen.append("1")
        else:
            oxygen.append("0")
    oxygen = find_entry(oxygen_running, size_e, 1)
    carbon = find_entry(co2_running, size_e, 0)
    oxygen = int(oxygen, 2)
    carbon = int(carbon, 2)
    return oxygen*carbon


def filter_values(running_list, i, value):
    new_list = list()
    for entry in running_list:
        if entry[i] == value:
            new_list.append(entry)
    return new_list


def find_entry(running, size_e, find_larger):
    for i in range(0, size_e):
        total1 = 0
        total0 = 0
        for line in running:
            char = line[i]
            if char == '1':
                total1 += 1
            else:
                total0 += 1

        value = "0"
        if find_larger:
            value = "1"
            if total1 < total0:
                value = "0"
        else:
            if total1 < total0:
                value = "1"
        running = filter_values(running, i, value)
        i += 1
        if len(running) == 1:
            return running[0]


def solve_day3(input_ls: list) -> list:
    output = list()
    part1 = solve_part1(input_ls)
    output.append(part1)
    part2 = solve_part2(input_ls)
    output.append(part2)
    return output
