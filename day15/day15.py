import copy


class Day15:
    # started 0:12 after
    def __init__(self, data):
        self.data = data
        self.iterations = 2021

    def solve_part1(self):
        turn_lookup = {}
        for idx, val in enumerate(self.data):
            turn_lookup[val] = idx + 1

        print(turn_lookup)

        # first turn after reading list:
        first_turn = len(self.data) + 1
        spoken = 0

        for turn in range(first_turn, self.iterations):
            if turn % 100000 == 1 or turn > self.iterations - 5:
                print(f"Turn {turn}, Spoken: {spoken}")
            if spoken in turn_lookup.keys():
                next_spoken = turn - turn_lookup[spoken]
                turn_lookup[spoken] = turn
            else:
                turn_lookup[spoken] = turn
                next_spoken = 0
            spoken = next_spoken

    def solve_part2(self):
        self.iterations = 30000001
        self.solve_part1()
