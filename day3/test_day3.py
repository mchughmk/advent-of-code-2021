from day3.day3 import DiagnosticReport


class TestDiagnosticReport:
    def test_most_common_bit_when_101_bit_1_expect_1(self):
        numbers = [5]
        expected = 1

        actual = DiagnosticReport.most_common_bit(numbers, 1)

        assert expected == actual

    def test_most_common_bit_when_101_bit_2_expect_0(self):
        numbers = [5]
        expected = 0

        actual = DiagnosticReport.most_common_bit(numbers, 2)

        assert expected == actual

    def test_most_common_bit_when_101_bit_3_expect_1(self):
        numbers = [5]
        expected = 1

        actual = DiagnosticReport.most_common_bit(numbers, 3)

        assert expected == actual

    def test_most_common_bit_when_input_101_001_000_bit_1_expect_1(self):
        numbers = [5, 1, 0]
        expected = 1

        actual = DiagnosticReport.most_common_bit(numbers, 1)

        assert expected == actual

    def test_most_common_bit_when_input_101_001_000_bit_2_expect_0(self):
        numbers = [5, 1, 0]
        expected = 0

        actual = DiagnosticReport.most_common_bit(numbers, 2)

        assert expected == actual

    def test_most_common_bit_when_input_101_001_000_bit_3_expect_0(self):
        numbers = [5, 1, 0]
        expected = 0

        actual = DiagnosticReport.most_common_bit(numbers, 3)

        assert expected == actual

    def test_gamma_rate_when_input_101_expect_5(self):
        diagnostic_report = DiagnosticReport(["101"])
        expected = 5

        actual = diagnostic_report.gamma_rate()

        assert expected == actual

    def test_gamma_rate_when_input_101_001_000_expect_1(self):
        diagnostic_report = DiagnosticReport(["101", "001", "000"])
        expected = 1

        actual = diagnostic_report.gamma_rate()

        assert expected == actual

    def test_epsilon_rate_when_input_101_expect_2(self):
        diagnostic_report = DiagnosticReport(["101"])
        expected = 2

        actual = diagnostic_report.epsilon_rate()

        assert expected == actual

    def test_oxygen_generator_rating_when_sample_expect_23(self):
        numbers = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        expected = 23
        diagnostic_report = DiagnosticReport(numbers)

        actual = diagnostic_report.oxygen_generator_rating()

        assert expected == actual

    def test_co2_scrubber_rating_when_sample_expect_10(self):
        numbers = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        expected = 10
        diagnostic_report = DiagnosticReport(numbers)

        actual = diagnostic_report.co2_scrubber_rating()

        assert expected == actual
