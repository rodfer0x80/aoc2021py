def format_vents(input_arr: list) -> list:
    vents = list()
    for vent in input_arr:
        vent_s, vent_e = vent.split(" -> ")

        vent_sx, vent_sy = vent_s.split(",")
        vent_ex, vent_ey = vent_e.split(",")

        vents.append([[int(vent_sx), int(vent_sy)], [int(vent_ex), int(vent_ey)]])
    return vents


def filter_diagonals(vents: list) -> list:
    filtered_vents = list()
    for vent in vents:
        x0 = vent[0][0]
        y0 = vent[0][1]
        x1 = vent[1][0]
        y1 = vent[1][1]
        if x0 == x1 or y0 == y1:
            filtered_vents.append(vent)
    return filtered_vents



def solve_part1(input_arr: list) -> int:
    vents = format_vents(input_arr)
    filtered_vents = filter_diagonals(vents)
    return 0

    
def solve_part2(input_arr: list) -> int:
    vents = format_vents(input_arr)
    filtered_vents = filter_diagonals(vents)
    return 0


def solve_day5(input_arr: list) -> list:
    output = []

    part1 = solve_part1(input_arr)
    output.append(part1)

    part2 = solve_part2(input_arr)
    output.append(part2)

    return output

