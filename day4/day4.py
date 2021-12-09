from os.path import dirname, join
import re
from utils import read_input


class BingoBoard:
    def __init__(self) -> None:
        self.rows = []
        self.has_won = False

    def sum_board(self) -> int:
        total = 0

        for row in self.rows:
            total += sum([num for num in row if num != "X"])

        return total

    def mark_number(self, number) -> None:
        self.rows = [
            ["X" if cell == number else cell for cell in row] for row in self.rows
        ]

    def has_winning_row(self) -> bool:
        for row in self.rows:
            if len([x for x in row if x == "X"]) == len(row):
                return True
        
        return False

    def has_winning_column(self) -> bool:
        for i in range(0, len(self.rows[0])):
            numberFound = False
            for row in self.rows:
                if row[i] != "X":
                    numberFound = True
                    break

            if not numberFound:
                return True

        return False

    def is_winner(self) -> bool:
        self.has_won = self.has_winning_row() or self.has_winning_column()

        return self.has_won

    
    def __str__(self) -> str:
        return str(self.rows)


def process_input(input):
    board = None
    boards = []
    for row in input:
        if ","  in row:
            numbers = [int(num) for num in row.split(",")]
        elif row == "":
            if board:
                boards.append(board)
            board = BingoBoard()
        else:
            board.rows.append([int(num) for num in re.split(r"\s+", row)])
        
    return (numbers, boards)


def main():
    input = read_input(join(dirname(__file__), "input.txt"))
    numbers, boards = process_input(input)

    final_score = 0
    num_winners = 0
    for number in numbers:
        for board in boards:
            if not board.has_won:
                board.mark_number(number)
                if board.is_winner():
                    num_winners += 1
                if num_winners == len(boards):
                    final_score = board.sum_board() * number
        
        if final_score > 0:
            break

    print(final_score)


if __name__ == "__main__":
    main()
