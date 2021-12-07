def find_medium_pos(input_arr: list) -> int:
    total = 0
    size_arr = len(input_arr)
    for i in input_arr:
        total += i
    medium_pos_m = total // size_arr
    medium_pos_p = medium_pos_m + 1
    print(medium_pos_p)
    print(medium_pos_m)
    return medium_pos_p, medium_pos_m

def calculate_fuel_usage(input_arr: list, medium_pos_p: int, medium_pos_n: int) -> int:
    fuel1 = 0
    fuel2 = 0
    for i in  input_arr:
        fuel1 += abs(medium_pos_p-i)
    for i in  input_arr:
        fuel2 += abs(medium_pos_n-i)
    if fuel1 < fuel2:
        fuel = fuel1 
    else:
        fuel = fuel2
    return fuel