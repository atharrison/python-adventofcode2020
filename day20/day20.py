import re
from collections import defaultdict
import math
from .tiles import Tile


class Day20:
    def __init__(self, data):
        self.raw_data = data
        self.tile_map = {}

    def solve_part1(self):
        self.load_tiles()
        print(f"Total Tiles: {len(self.tile_map)}")

        used_tiles = []
        unused_tiles = self.tile_map.keys()
        partial_solution = []

        self.recursive_solve(used_tiles, unused_tiles, partial_solution)

    def recursive_solve(self, used_tiles, unused_tiles, partial_solution):
        for x, y in self.diagonal_iteration(int(math.sqrt(len(self.tile_map)))):
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

    def load_tiles(self):
        tile_header_pattern = re.compile(r"^Tile (\d+):")
        for line in self.raw_data:

            if len(line) == 0:
                # print(tile)
                continue

            tile_match = tile_header_pattern.match(line)
            if tile_match:
                tile_num = tile_match[1]
                # print(tile_num)
                tile = Tile(tile_num)
                self.tile_map[tile_num] = tile
            else:
                tile.add_line(line)
