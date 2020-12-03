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

    def solve_part2(self):
        # brute force
        calculations = 0
        for item1 in self.data:
            for item2 in self.data:
                for item3 in self.data:
                    calculations += 1
                    if int(item1) + int(item2) + int(item3) == 2020:
                        print(f"Solution: {int(item1) * int(item2) * int(item3)}")
                        print(f"Calculations: {calculations}")
                        # Brute calcs: Calculations: 685861
                        return

    def solve_part2_efficient(self):
        calculations = 0
        int_data = [int(d) for d in self.data]
        int_data.sort()
        input_len = len(int_data)
        idx1 = 0
        idx2 = 1
        idx3 = 2

        while True:
            num1 = int_data[idx1]
            num2 = int_data[idx2]
            num3 = int_data[idx3]
            calculations += 1
            sum = num1 + num2 + num3
            if sum == 2020:
                print(f"Solution: {num1 * num2 * num3}")
                print(f"Calculations: {calculations}")
                # Efficient calcs: Calculations: 601 (plus data.sort(), sort-only)
                # Efficient calcs: Calculations: 51 (plus data.sort() and checking for overage)
                return
            else:
                if sum > 2020:
                    idx3 = input_len
                else:
                    idx3 += 1

                if idx3 == input_len:
                    idx2 += 1
                    if idx2 == input_len < 1:
                        idx1 += 1
                        idx2 = idx1 + 1
                        idx3 = idx2 + 1
                        if idx1 == input_len - 2:
                            print("No solution found.")
                            return
                    else:
                        idx3 = idx2 + 1

    def solve_part2_efficient2(self):
        calculations = 0
        int_data = [int(d) for d in self.data]
        int_data.sort()

        # logic re-written back into for-loops, with inner-break to short-circuit impossible calcs.
        for idx1, num1 in enumerate(int_data):
            for idx2, num2 in enumerate(int_data):
                if idx2 <= idx1:
                    continue
                try:
                    for idx3, num3 in enumerate(int_data):
                        if idx3 <= idx2:
                            continue

                        calculations += 1
                        sum = num1 + num2 + num3
                        if sum == 2020:
                            print(f"Solution: {num1 * num2 * num3}")
                            print(f"Calculations: {calculations}")
                            # Efficient calcs: Calculations: 601 (plus data.sort(), sort-only)
                            # Efficient calcs: Calculations: 51 (plus data.sort() and checking for overage)
                            return
                        if sum > 2020:
                            raise StopIteration
                except StopIteration:
                    pass

        print("No solution found.")
