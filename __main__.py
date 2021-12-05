from sys import stderr, exit

from utils.args import Args
from utils.utils import Utils

from src.day0 import solve_day0
from src.day1 import solve_day1
from src.day2 import solve_day2
from src.day3 import solve_day3


if __name__ == '__main__':
    args = Args()
    args.get_args()

    utils = Utils()
    utils.select_day(args.day)
    day = utils.get_day()
    del args

    
    if day == 0:
        utils.read_input("it")
        output = solve_day0(utils.input_arr)
    elif day == 1:
        utils.read_input("int")
        output = solve_day1(utils.input_arr)
    elif day == 2:
        utils.read_input("str")
        output = solve_day2(utils.input_arr)
    elif day == 3:
        utils.read_input("str")
        output = solve_day3(utils.input_arr)
    else:
        stderr.write("[!] Unknown error")

    utils.write_output(output)
    exit(0)

