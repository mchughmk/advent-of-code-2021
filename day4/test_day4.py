from day4.day4 import BingoBoard


class TestBingoBoard:
    def setup_method(self, method):
        self.board = BingoBoard()

    def test_sum_board_when_no_numbers_expect_0(self):
        expected = 0

        actual = self.board.sum_board()

        assert actual == expected

    def test_sum_board_when_one_item_expect_1(self):
        self.board.rows = [[1]]
        expected = 1

        actual = self.board.sum_board()

        assert actual == expected

    def test_sumb_board_when_two_items_expect_2(self):
        self.board.rows = [[1, 1]]
        expected = 2

        actual = self.board.sum_board()

        assert actual == expected

    def test_sum_board_when_two_rows_of_two_items_expect_4(self):
        self.board.rows = [[1, 1], [1, 1]]
        expected = 4

        actual = self.board.sum_board()

        assert actual == expected

    def test_sum_board_when_two_rows_and_one_item_marked_expect_3(self):
        self.board.rows = [[1, 1], ["X", 1]]
        expected = 3

        actual = self.board.sum_board()

        assert actual == expected

    def test_mark_number_when_in_board_expect_replaced_with_X(self):
        self.board.rows = [[1, 2], [3, 4]]
        expected = [[1, 2], ["X", 4]]

        actual = self.board.mark_number(3)

        assert self.board.rows == expected

    def test_mark_number_when_not_in_board_expect_no_replacement(self):
        self.board.rows = [[1, 2], [3, 4]]
        expected = [[1, 2], [3, 4]]

        actual = self.board.mark_number(5)

        assert self.board.rows == expected

    def test_has_winning_row_when_no_spaces_marked_expect_false(self):
        self.board.rows = [[1, 2], [3, 4]]
        expected = False

        actual = self.board.has_winning_row()

        assert actual == expected

    def test_has_winning_row_when_one_space_marked_expect_false(self):
        self.board.rows = [[1, "X"], [3, 4]]
        expected = False

        actual = self.board.has_winning_row()

        assert actual == expected

    def test_has_winning_row_when_two_spaces_marked_expect_true(self):
        self.board.rows = [["X", "X"], [3, 4]]
        expected = True

        actual = self.board.has_winning_row()

        assert actual == expected

    def test_has_winning_row_when_last_row_marked_expect_true(self):
        self.board.rows = [[1, 2], ["X", "X"]]
        expected = True

        actual = self.board.has_winning_row()

        assert actual == expected

    def test_has_winning_column_when_no_spaces_marked_expect_false(self):
        self.board.rows = [[1, 2], [3, 4]]
        expected = False

        actual = self.board.has_winning_column()

        assert actual == expected

    def test_has_winning_column_when_one_space_marked_expect_false(self):
        self.board.rows = [["X", 2], [3, 4]]
        expected = False

        actual = self.board.has_winning_column()

        assert actual == expected

    def test_has_winning_column_when_two_spaces_marked_expect_true(self):
        self.board.rows = [["X", 2], ["X", 4]]
        expected = True

        actual = self.board.has_winning_column()

        assert actual == expected

    def test_has_winning_column_when_last_column_marked_expect_true(self):
        self.board.rows = [[1, "X"], [3, "X"]]
        expected = True

        actual = self.board.has_winning_column()

        assert actual == expected

    def test_is_winner_when_no_numbers_marked_expect_false(self):
        self.board.rows = [[1, 2], [3, 4]]
        expected = False

        actual = self.board.is_winner()

        assert actual == expected

    def test_is_winner_when_one_number_marked_expect_false(self):
        self.board.rows = [[1, "X"], [3, 4]]
        expected = False

        actual = self.board.is_winner()

        assert actual == expected

    def test_is_winner_when_winning_row_expect_true(self):
        self.board.rows = [["X", "X"], [3, 4]]
        expected = True

        actual = self.board.is_winner()

        assert actual == expected

    def test_is_winner_when_winning_column_expect_true(self):
        self.board.rows = [["X", 2], ["X", 4]]
        expected = True

        actual = self.board.is_winner()

        assert actual == expected