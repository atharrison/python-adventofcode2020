from .interpreter import EqualPrecedenceInterpreter


class Day18:
    # Started 0:35 after
    def __init__(self, data):
        self.raw_data = data
        self.interpreter = EqualPrecedenceInterpreter()

    def solve_part1(self):
        total = 0
        for line in self.raw_data:
            line_result = self.interpreter.solve(line.replace(" ", ""))
            print(f"Line Result: {line_result}")
            total += line_result

        print(f"Line Sum Total: {total}")

    def solve_part2(self):
        total = 0
        for line in self.raw_data:
            line_result = self.interpreter.regroup_solve(line.replace(" ", ""))
            print(f"Line Result: {line_result}")
            total += line_result

        print(f"Line Sum Total: {total}")
