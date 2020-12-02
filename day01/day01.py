class Day01:
    def __init__(self, data):
        self.data = data

    def solve_part1(self):
        # brute force
        for item1 in self.data:
            for item2 in self.data:
                if int(item1) + int(item2) == 2020:
                    print(f"Solution: {int(item1) * int(item2)}")
                    return
