from sys import stderr, exit

from utils.args import Args
from utils.utils import Utils

from src.day0 import solve_day0
from src.day1 import solve_day1
from src.day2 import solve_day2
from src.day3 import solve_day3
from src.day4 import solve_day4
from src.day5 import solve_day5
from src.day6 import solve_day6
from src.day7 import solve_day7
from src.day8 import solve_day8
from src.day9 import solve_day9
from src.day10 import solve_day10
from src.day11 import solve_day11
from src.day12 import solve_day12
from src.day13 import solve_day13
from src.day14 import solve_day14


if __name__ == '__main__':
    args = Args()
    args.get_args()

    utils = Utils()
    utils.select_day(args.day)
    day = utils.get_day()
    del args

    
    if day == 0:
        utils.read_input("it")
        output = solve_day0(utils.input_ls)
    elif day == 1:
        utils.read_input("int")
        output = solve_day1(utils.input_ls)
    elif day == 2:
        utils.read_input("str")
        output = solve_day2(utils.input_ls)
    elif day == 3:
        utils.read_input("str")
        output = solve_day3(utils.input_ls)
    elif day == 4:
        utils.read_input("str")
        output = solve_day4(utils.input_ls)
    elif day == 5:
        utils.read_input("str")
        output = solve_day5(utils.input_ls)
    elif day == 6:
        utils.read_input("csv/int")
        output = solve_day6(utils.input_ls)
    elif day == 7:
        utils.read_input("csv/int")
        output = solve_day7(utils.input_ls)
    elif day == 8:
        utils.read_input("str")
        output = solve_day8(utils.input_ls)
    elif day == 9:
        utils.read_input("str")
        output = solve_day9(utils.input_ls)
    elif day == 10:
        utils.read_input("str")
        output = solve_day10(utils.input_ls)
    elif day == 11:
        utils.read_input("str")
        output = solve_day11(utils.input_ls)
    elif day == 12:
        utils.read_input("str")
        output = solve_day12(utils.input_ls)
    elif day == 13:
        utils.read_input("str")
        output = solve_day13(utils.input_ls)
    elif day == 14:
        utils.read_input("str")
        output = solve_day14(utils.input_ls)
    else:
        stderr.write("[!] Unknown error")

    utils.write_output(output)
    exit(0)










