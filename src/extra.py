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


from sys import stderr, exit, stdout
from functools import lru_cache


@lru_cache(maxsize=32768)
class Cycle:
    def __init__(self, order: str, cycle_zero: int, cycle_peak: int, ptr: int):
        self.order = order
        if self.order != "ascending" and self.order != "descending":
            self.print_error("'order' argument is incorrect")
        self.cycle_zero = cycle_zero
        self.cycle_peak = cycle_peak
        self.cycle = self.build_cycle()
        self.ptr = ptr
    
    def print_error(error: str):
        stderr.write(f"[!] Fatal creating cycle class: {error}")
        exit(0)

    def build_cycle(self):
        cycle: list = []
        nxt: int = 0
        if self.order == "descending":
            for i in range(self.cycle_peak, self.cycle_zero-1, -1):
                nxt = i-1
                if nxt == self.cycle_zero-1:
                    nxt = self.cycle_peak

                cycle.append([i, nxt])
        elif self.order == "ascending":
            for i in range(self.cycle_zero, self.cycle_peak+1):
                nxt = i-1
                if nxt == self.cycle_zero-1:
                    nxt = self.cycle_peak

                cycle.append([i, nxt])
        else:
            self.print_error("'order' argument is incorrect")
        return cycle
    
    def this(self):
        return str(self.cycle[self.ptr][0])

    def tick(self):
        if self.order == "descending":
            self.ptr -= 1
        elif self.order == "ascending":
            self.ptr += 1
        else:
            self.print_error("'order' argument is incorrect")
        if self.ptr == self.cycle_zero-1:
            self.ptr = self.cycle_peak
        return str(self.cycle[self.ptr][0])


@lru_cache(maxsize=32768)
class Fishpool:
    def __init__(self):
        self.fishpool = []
        self.count = 0
        
    def add_fish(self, newfish):
        self.fishpool.append(newfish)
        self.count += 1


@lru_cache(maxsize=32768)
class Lanterfish:
    def __init__(self, day_count, fishpool):
        self.fishpool = fishpool
        self.day_count = day_count
        self.cycle = Cycle("descending", 0, 6, self.day_count)
        self.this = self.cycle.this()
        while int(self.this) != self.day_count:
            self.this = self.cycle.tick()
        self.newborn = False

    def tick(self):
        nxt = int(self.cycle.tick())
        if nxt == 0:
            self.newborn = True
            self.newborn_count = 2
        if self.newborn == True:
            self.newborn_count -= 1
            if self.newborn_count == 0:
                newfish = Lanterfish(6, self.fishpool)
                self.fishpool.add_fish(newfish)
        
def multisolve(occurrences, input_arr):
    fishpool: list = input_arr
    new_fishpool:list
    newborn_fishpool: list
    for i in range(occurrences):
        print(f"Day: {i+1}")
        stdout.flush()
        new_fishpool = []
        newborn_fishpool = []
        for fish in fishpool:
            fish -= 1
            if fish == -1:
                fish = 6
                newfish = 8
                newborn_fishpool.append(newfish)
            new_fishpool.append(fish)
        fishpool = new_fishpool + newborn_fishpool
    return len(fishpool)