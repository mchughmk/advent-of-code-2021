from os.path import dirname, join
from utils import read_input


class Point:
    def __init__(self, x=None, y=None, point_str=None) -> None:
        if point_str:
            split = point_str.split(",")
            self.x = int(split[0])
            self.y = int(split[1])
        else:
            self.x = x
            self.y = y

    def __eq__(self, other: object) -> bool:
        return ((self.x, self.y) == (other.x, other.y))

    def __ne__(self, other: object) -> bool:
        return ((self.x, self.y) != (other.x, other.y))

    def __lt__(self, other: object) -> bool:
        return ((self.x, self.y) < (other.x, other.y))

    def __lte__(self, other: object) -> bool:
        return ((self.x, self.y) <= (other.x, other.y))

    def __gt__(self, other: object) -> bool:
        return ((self.x, self.y) > (other.x, other.y))

    def __gte__(self, other: object) -> bool:
        return ((self.x, self.y) >= (other.x, other.y))

    def __repr__(self) -> str:
        return f"{self.x},{self.y}"


class Line:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def get_line_points(self) -> list[Point]:
        if self.is_horizontal():
            step = int((self.end.x - self.start.x) / abs(self.end.x - self.start.x))
            return [Point(x=x, y=self.start.y) for x in range(self.start.x, self.end.x + step, step)]
        elif self.is_vertical():
            step = int((self.end.y - self.start.y) / abs(self.end.y - self.start.y))
            return [Point(x=self.start.x, y=y) for y in range(self.start.y, self.end.y + step, step)]
        else:
            x_step = int((self.end.x - self.start.x) / abs(self.end.x - self.start.x))
            y_step = int((self.end.y - self.start.y) / abs(self.end.y - self.start.y))
            return [
                Point(x=self.start.x + x_step*i, y=self.start.y + y_step*i)
                for i in range(abs(self.end.x - self.start.x) + 1)
            ]

    def __repr__(self) -> str:
        return f"Start: {self.start}; End {self.end}"


def process_input(line) -> Line:
    points_split = line.split(" -> ")
    return Line(Point(point_str=points_split[0]), Point(point_str=points_split[1]))


def find_overlap(lines: list[Line]) -> int:
    plots = {}

    for line in lines:
        for point in line.get_line_points():
            key = str(point)
            if key not in plots.keys():
                plots[key] = 1
            else:
                plots[key] += 1

    return len([k for (k,v) in plots.items() if v > 1])


def main():
    lines = read_input(join(dirname(__file__), "input.txt"), process_input)
    
    num_overlaps = find_overlap(lines)

    print(num_overlaps)

if __name__ == "__main__":
    main()