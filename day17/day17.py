from collections import defaultdict


class Day17:
    def __init__(self, data):
        # started 1:00 after release
        self.raw_data = data

        self.four_pocket = defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
        )
        self.three_pocket = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
        self.max_size = 0

    def solve_part1(self):
        rounds = 6
        self.load_initial_3state(rounds=rounds)

        for r in range(rounds):
            self.three_pocket = self.update_pocket3(self.three_pocket)

        total_active = 0
        for xx in range(self.max_size):
            for yy in range(self.max_size):
                for zz in range(self.max_size):
                    if self.three_pocket[zz][yy][xx] == "#":
                        total_active += 1

        print(f"Total Active after {rounds} rounds: {total_active}")

    def update_pocket3(self, pocket):
        new_pocket = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
        for x in range(self.max_size):
            for y in range(self.max_size):
                for z in range(self.max_size):
                    new_pocket[z][y][x] = self.next_3state_for(x, y, z, pocket)

        return new_pocket

    def next_3state_for(self, x, y, z, pocket):
        neighbors = 0
        for xx in [x - 1, x, x + 1]:
            for yy in [y - 1, y, y + 1]:
                for zz in [z - 1, z, z + 1]:
                    if xx == x and yy == y and zz == z:
                        continue
                    if pocket[zz][yy][xx] == "#":
                        neighbors += 1

        if pocket[z][y][x] == "#":
            if neighbors == 2 or neighbors == 3:
                return "#"
            else:
                return "."

        else:
            if neighbors == 3:
                return "#"
            else:
                return "."

    def load_initial_3state(self, rounds):
        size = 0
        z = 0
        for y, line in enumerate(self.raw_data):
            if size == 0:
                size = len(line)
                self.max_size = size + rounds * 2
                self.middle = self.max_size // 2
                z = rounds
                for zz in range(self.max_size):
                    for yy in range(self.max_size):
                        for xx in range(self.max_size):
                            self.three_pocket[zz][yy][xx] = "."

            row = ["."] * rounds
            row += [char for char in line]
            row += ["."] * rounds
            print(f"adding row {row}")
            for x, char in enumerate(row):
                self.three_pocket[z][y + rounds][x] = char

    def solve_part2(self):
        rounds = 6
        self.load_initial_4state(rounds=rounds)

        for r in range(rounds):
            self.four_pocket = self.update_pocket4(self.four_pocket)

        total_active = 0
        for xx in range(self.max_size):
            for yy in range(self.max_size):
                for zz in range(self.max_size):
                    for ww in range(self.max_size):
                        if self.four_pocket[ww][zz][yy][xx] == "#":
                            total_active += 1

        print(f"Total Active after {rounds} rounds: {total_active}")

    def update_pocket4(self, pocket):
        new_pocket = defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
        )
        for x in range(self.max_size):
            for y in range(self.max_size):
                for z in range(self.max_size):
                    for w in range(self.max_size):
                        new_pocket[w][z][y][x] = self.next_4state_for(
                            x, y, z, w, pocket
                        )

        return new_pocket

    def next_4state_for(self, x, y, z, w, pocket):
        neighbors = 0
        for xx in [x - 1, x, x + 1]:
            for yy in [y - 1, y, y + 1]:
                for zz in [z - 1, z, z + 1]:
                    for ww in [w - 1, w, w + 1]:
                        if xx == x and yy == y and zz == z and ww == w:
                            continue
                        if pocket[ww][zz][yy][xx] == "#":
                            neighbors += 1

        if pocket[w][z][y][x] == "#":
            if neighbors == 2 or neighbors == 3:
                return "#"
            else:
                return "."

        else:
            if neighbors == 3:
                return "#"
            else:
                return "."

    def load_initial_4state(self, rounds):
        size = 0
        z = 0
        w = 0
        for y, line in enumerate(self.raw_data):
            if size == 0:
                size = len(line)
                self.max_size = size + rounds * 2
                self.middle = self.max_size // 2
                z = rounds
                w = rounds
                for ww in range(self.max_size):
                    for zz in range(self.max_size):
                        for yy in range(self.max_size):
                            for xx in range(self.max_size):
                                self.four_pocket[ww][zz][yy][xx] = "."

            row = ["."] * rounds
            row += [char for char in line]
            row += ["."] * rounds
            print(f"adding row {row}")
            for x, char in enumerate(row):
                self.four_pocket[w][z][y + rounds][x] = char
