from os.path import dirname, join
from utils import read_input


def decode_segments(readings) -> dict:
    numbers = [""]*10

    for reading in readings:
        if len(reading) == 2:
            numbers[1] = reading
        elif len(reading) == 3:
            numbers[7] = reading
        elif len(reading) == 4:
            numbers[4] = reading
        elif len(reading) == 7:
            numbers[8] = reading

    for reading in filter(lambda x:len(x) == 6, readings):
        if all(s in reading for s in numbers[4]):
            numbers[9] = reading
        elif all(s in reading for s in numbers[7]):
            numbers[0] = reading
        else:
            numbers[6] = reading

    for reading in filter(lambda x:len(x) == 5, readings):
        if all(s in reading for s in numbers[1]):
            numbers[3] = reading
        elif len([s for s in numbers[9] if s not in reading]) == 1:
            numbers[5] = reading
        else: 
            numbers[2] = reading

    return {num:str(i) for i, num in enumerate(numbers)}


def determine_output(code, output_values):
    return int("".join([code[x] for x in output_values]))


def split_and_sort(input) -> list[str]:
    return ["".join(sorted(s, key=lambda x:x.lower())) for s in input.split()]


def process_input(input) -> list[list[str]]:
    return [split_and_sort(x) for x in input.split("|")]


def main():
    logs = read_input(join(dirname(__file__), "input.txt"), process_input)

    total = 0
    for log in logs:
        code = decode_segments(log[0])
        total += determine_output(code, log[1])

    print(total)


if __name__ == "__main__":
    main()