from day5.day5 import Line, Point, find_overlap

class TestLine:
    def setup_method(self, method):
        self.horizontal_line = Line(Point(x=0, y=0), Point(x=2, y=0))
        self.vertical_line = Line(Point(x=0, y=0), Point(x=0, y=2))

    def test_is_vertical_when_y_changes_expect_true(self):
        expected = True

        actual = self.vertical_line.is_vertical()

        assert expected == actual

    def test_is_vertical_when_y_does_not_change_expect_false(self):
        expected = False

        actual = self.horizontal_line.is_vertical()

        assert expected == actual

    def test_is_horizontal_when_x_changes_expect_true(self):
        expected = True

        actual = self.horizontal_line.is_horizontal()

        assert expected == actual

    def test_is_horizontal_when_x_does_not_change_expect_false(self):
        expected = False

        actual = self.vertical_line.is_horizontal()

        assert expected == actual

    def test_get_line_points_when_x_increases_expect_00_10_20(self):
        expected = [Point(x=0, y=0), Point(x=1, y=0), Point(x=2, y=0)]

        actual = self.horizontal_line.get_line_points()

        assert expected == actual

    def test_get_line_points_when_y_increases_expect_00_01_02(self):
        expected = [Point(x=0, y=0), Point(x=0, y=1), Point(x=0, y=2)]

        actual = self.vertical_line.get_line_points()

        assert expected == actual

    def test_get_line_points_when_x_decreases_expect_20_10_00(self):
        line = Line(Point(x=2, y=0), Point(x=0, y=0))
        expected = [Point(x=2, y=0), Point(x=1, y=0), Point(x=0, y=0)]

        actual = line.get_line_points()

        assert expected == actual

    def test_get_line_points_when_y_decreases_expect_02_01_00(self):
        line = Line(Point(x=0, y=2), Point(x=0, y=0))
        expected = [Point(x=0, y=2), Point(x=0, y=1), Point(x=0, y=0)]

        actual = line.get_line_points()

        assert expected == actual


class TestFindOverlap:
    def test_find_overlap_when_no_overlap_expect_0(self):
        lines = [
            Line(Point(x=0, y=0), Point(x=0, y=1)),
            Line(Point(x=1, y=0), Point(x=1, y=1))
        ]
        expected = 0

        actual = find_overlap(lines)

        assert expected == actual

    def test_find_overlap_when_one_point_overlap_expect_1(self):
        lines = [
            Line(Point(x=0, y=0), Point(x=0, y=1)),
            Line(Point(x=0, y=1), Point(x=2, y=1))
        ]
        expected = 1

        actual = find_overlap(lines)

        assert expected == actual

    def test_find_overlap_sample_scenario_expect_5(self):
        lines = [
            Line(Point(x=0, y=9), Point(x=5, y=9)),
            Line(Point(x=8, y=0), Point(x=0, y=8)),
            Line(Point(x=9, y=4), Point(x=3, y=4)),
            Line(Point(x=2, y=2), Point(x=2, y=1)),
            Line(Point(x=7, y=0), Point(x=7, y=4)),
            Line(Point(x=6, y=4), Point(x=2, y=0)),
            Line(Point(x=0, y=9), Point(x=2, y=9)),
            Line(Point(x=3, y=4), Point(x=1, y=4)),
            Line(Point(x=0, y=0), Point(x=8, y=8)),
            Line(Point(x=5, y=5), Point(x=8, y=2))
        ]
        expected = 12

        actual = find_overlap(lines)

        assert expected == actual