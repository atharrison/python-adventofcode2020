class IntCode:
    def __init__(self):
        self.instructions = []

        self.accumulator = 0
        self.change_instr_ptr = 0
        self.swapped = False

    def __str__(self):
        return f"{self.instructions}"

    def reset(self):
        self.accumulator = 0

    def add_instruction(self, instr):
        self.instructions.append(instr)

    def find_next_to_swap(self):
        print(f"Looking for next to swap. At {self.change_instr_ptr}")
        self.change_instr_ptr += 1
        while self.instructions[self.change_instr_ptr].op == "acc":
            self.change_instr_ptr += 1

    def run_until_loop(self):
        ptr = 0
        used_ptrs = set()
        while not ptr in used_ptrs:
            used_ptrs.add(ptr)
            ptr = ptr + self.execute_instr(self.instructions[ptr])
            if ptr in used_ptrs:
                return self.accumulator

    def run_until_loop_or_exit(self):
        count = 0
        ptr = 0
        used_ptrs = set()
        while not ptr in used_ptrs:
            used_ptrs.add(ptr)
            ptr = ptr + self.execute_instr(self.instructions[ptr])
            count += 1
            if ptr in used_ptrs:
                print(f"Looped after {count}")
                return True
            elif ptr >= len(self.instructions):
                print(f"Terminated after {count}")
                return False

    def execute_instr(self, instr):
        return instr.execute(self)

    def ends_in_loop(self):
        return self.run_until_loop_or_exit()

    def change_next_instr(self):
        if self.swapped:
            self.instructions[self.change_instr_ptr].swap()
            self.swapped = False
            self.find_next_to_swap()
        else:
            self.instructions[self.change_instr_ptr].swap()
            self.swapped = True


class Instruction:
    def __init__(self, line, line_number):
        self.line = line
        self.lineno = line_number

        chunks = self.line.split(" ")
        self.op = chunks[0]

        self.num = int(chunks[1][1:])
        if chunks[1][0] == "-":
            self.num = 0 - self.num

    def execute(self, intcode):
        # print(f"EX: {self.line} - {self.op} {self.num} ...")
        if self.op == "nop":
            return 1
        elif self.op == "acc":
            intcode.accumulator += self.num
            return 1
        elif self.op == "jmp":
            return self.num

    def swap(self):
        if self.op == "nop":
            self.op = "jmp"
            print(f"Swapping {self.lineno}:{self.line} to jmp ...")
        else:
            self.op = "nop"
            print(f"Swapping {self.lineno}:{self.line} to nop ...")

    def __str__(self):
        return f"{self.lineno}:{self.line} - {self.op}|{self.num}"

    def __repr__(self):
        return self.__str__()
