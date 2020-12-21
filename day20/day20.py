from collections import defaultdict


class Day20:
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        for x, y in self.diagonal_iteration(3):
            print(f"Generated [{x},{y}]")

    def diagonal_iteration(self, size):
        """
        Iterate over a two-dimensional matrix diagonally
        Starting with [0, 0] and ending at [size-1, size-1]
        """
        for a in range(0, size, 1):
            for b in range(a + 1, 0, -1):
                x = a - b + 1
                y = b - 1
                yield x, y

        for a in range(0, size, 1):
            for b in range(size - a - 1, 0, -1):
                x = size - b
                y = b + a
                yield x, y

    def solve_part2(self):
        pass
