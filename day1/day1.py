from os.path import dirname, join
from utils import read_input


def depth_increases(measurements):
    increases = [
        measurements[i]
        for i in range(1, len(measurements))
        if measurements[i] > measurements[i - 1]
    ]

    return len(increases)


def measurement_sets(measurements):
    return [
        sum([measurements[i], measurements[i - 1], measurements[i - 2]])
        for i in range(2, len(measurements))
    ]


def main():
    measurements = read_input(
        join(dirname(__file__), "input.txt"), lambda line: int(line)
    )
    print(f"Total Increases: {depth_increases(measurements)}")
    print(f"Total Set Increases: {depth_increases(measurement_sets(measurements))}")


if __name__ == "__main__":
    main()
