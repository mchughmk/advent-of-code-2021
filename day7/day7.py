from os.path import dirname, join
from utils import read_input


def fuel_cost(current_location, target_location):
    return sum(range(1, abs(current_location - target_location)+1))


def align_horizontally(crabs):
    lowest_fuel = None

    for position in range(1, max(crabs)+1):
        fuel_required = sum([fuel_cost(crab, position) for crab in crabs])
        if not lowest_fuel or fuel_required < lowest_fuel:
            lowest_fuel = fuel_required
    
    return lowest_fuel if lowest_fuel else 0


def process_input(input) -> list[int]:
    return [int(x) for x in input.split(",")]


def main():
    lines = read_input(join(dirname(__file__), "input.txt"))
    crab_positions = process_input(lines[0])

    print(align_horizontally(crab_positions))


if __name__ == "__main__":
    main()