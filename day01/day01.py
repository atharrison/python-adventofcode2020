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
            if num1 + num2 + num3 == 2020:
                print(f"Solution: {num1 * num2 * num3}")
                print(f"Calculations: {calculations}")
                # Efficient calcs: Calculations: 601 (plus data.sort())
                return
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
