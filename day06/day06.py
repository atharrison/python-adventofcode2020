import re


class Day06:
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        groups = self.load_groups()

        total = 0
        for g in groups:
            print(list(g.replace(" ", "")))
            s = set(list(g))
            s.discard(" ")
            print(s)
            print(len(s))
            total += len(s)

        print(total)

    def solve_part2(self):
        groups = self.load_groups()

        total = 0
        for g in groups:
            if len(g) == 0:
                continue
            intersection = list("abcdefghijklmnopqrstuvwxyz")
            subgroups = g.split(" ")
            for sub in subgroups:
                if len(sub) == 0:
                    continue
                intersection = [value for value in sub if value in intersection]

            print(list(g))
            print(intersection)
            total += len(intersection)

        print(total)

    def load_groups(self):
        groups = []
        multiline = ""
        for line in self.raw_data:
            if len(line) == 0:
                groups.append(multiline)
                multiline = ""
            else:
                multiline = multiline + " " + line

        groups.append(multiline)
        return groups
