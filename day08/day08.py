from .intcode import IntCode, Instruction


class Day08:
    # Started 1:48 later than start.
    def __init__(self, data):
        self.raw_data = data
        self.intcode = IntCode()

    def solve_part1(self):
        self.load_intcode()
        result = self.intcode.run_until_loop()
        print(f"Result: {result}")

    def solve_part2(self):
        self.intcode = IntCode()
        self.load_intcode()
        print(self.load_intcode)
        self.intcode.find_next_to_swap()
        while self.intcode.ends_in_loop():
            self.intcode.reset()
            self.intcode.change_next_instr()

        print(f"Result: {self.intcode.accumulator}")

    def load_intcode(self):
        for idx, line in enumerate(self.raw_data):
            self.intcode.add_instruction(Instruction(line, idx))
