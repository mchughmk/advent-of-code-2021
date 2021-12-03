from os.path import dirname, join
from utils import read_input


class Instruction:
    def __init__(self, direction: str, amount: int) -> None:
        self.direction = direction
        self.amount = amount


class Submarine:
    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def process_instruction(self, instruction: Instruction) -> None:
        if instruction.direction == "up":
            self.aim -= instruction.amount
        elif instruction.direction == "down":
            self.aim += instruction.amount
        elif instruction.direction == "forward":
            self.horizontal += instruction.amount
            self.depth += self.aim * instruction.amount

    def __str__(self) -> str:
        return f"Horizontal: {self.horizontal}, Depth: {self.depth}\nProduct: {self.horizontal * self.depth}"


def parse_instruction(instruction_input: str) -> Instruction:
    parts = instruction_input.split(" ")
    if len(parts) == 2:
        return Instruction(parts[0], int(parts[1]))

    return Instruction()


def main():
    sub = Submarine()
    instructions = read_input(join(dirname(__file__), "input.txt"), parse_instruction)

    for instruction in instructions:
        sub.process_instruction(instruction)

    print(sub)


if __name__ == "__main__":
    main()
