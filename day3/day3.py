from math import pow
from os.path import dirname, join
from utils import read_input


class DiagnosticReport:
    def __init__(self, report_numbers) -> None:
        self.bit_length = len(report_numbers[0]) if len(report_numbers) > 0 else 0
        self.report_numbers = [int(num, 2) for num in report_numbers]
        self.num_inputs = len(report_numbers)

    @classmethod
    def most_common_bit(cls, numbers, bit):
        mask = int(pow(2, bit - 1))
        sum = 0

        for num in numbers:
            sum += 1 if num & mask else 0

        return 1 if sum >= len(numbers) / 2 else 0

    @classmethod
    def least_common_bit(cls, numbers, bit):
        return not DiagnosticReport.most_common_bit(numbers, bit)

    def gamma_rate(self):
        binary = "".join(
            [
                str(DiagnosticReport.most_common_bit(self.report_numbers, bit))
                for bit in range(self.bit_length, 0, -1)
            ]
        )

        return int(binary, 2)

    def epsilon_rate(self):
        mask = int(pow(2, self.bit_length)) - 1

        return self.gamma_rate() ^ mask

    def oxygen_generator_rating(self, numbers=None, bit=None):
        if not numbers:
            numbers = self.report_numbers
        if not bit:
            bit = self.bit_length

        if len(numbers) == 1:
            return numbers[0]

        mask = int(pow(2, bit - 1))
        most_common = DiagnosticReport.most_common_bit(numbers, bit)
        remaining_nums = [num for num in numbers if num & mask == most_common * mask]

        return self.oxygen_generator_rating(remaining_nums, bit - 1)

    def co2_scrubber_rating(self, numbers=None, bit=None):
        if not numbers:
            numbers = self.report_numbers
        if not bit:
            bit = self.bit_length

        if len(numbers) == 1:
            return numbers[0]

        mask = int(pow(2, bit - 1))
        least_common = DiagnosticReport.least_common_bit(numbers, bit)
        remaining_nums = [num for num in numbers if num & mask == least_common * mask]

        return self.co2_scrubber_rating(remaining_nums, bit - 1)

    def __str__(self) -> str:
        oxygen_rating = self.oxygen_generator_rating()
        co2_rating = self.co2_scrubber_rating()
        return f"Oxygen Rating: {oxygen_rating}, CO2 Rating: {co2_rating}\nProduct: {oxygen_rating * co2_rating}"


def main():
    reports = read_input(join(dirname(__file__), "input.txt"))
    diagnostic_report = DiagnosticReport(reports)
    print(diagnostic_report)


if __name__ == "__main__":
    main()
