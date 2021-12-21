from os.path import dirname, join
from utils import read_input


def cycle_day(fish_state: list[int]) -> list[int]:
    new_state = fish_state[1:] + fish_state[:1]
    new_state[6] += new_state[8]

    return new_state


def model_scenario(initial_state: list[int], num_days: int) -> int:
    fish_state = [0]*9
    for fish in initial_state:
        fish_state[fish] += 1

    for day in range(num_days):
        fish_state = cycle_day(fish_state)

    return sum(fish_state)


def process_input(input) -> list[int]:
    return [int(x) for x in input.split(",")]


def main():
    lines = read_input(join(dirname(__file__), "input.txt"))
    fish_state = process_input(lines[0])

    print(model_scenario(fish_state, 256))


if __name__ == "__main__":
    main()