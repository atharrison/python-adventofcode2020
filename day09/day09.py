class Day09:
    # Started 0:27 later than start.
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        start = 0
        end = 24
        # end = 4
        numbers = [int(d) for d in self.raw_data]
        solution = 0
        while end < len(numbers):
            valid_sum = self.find_sum(numbers[start : end + 1], numbers[end + 1])
            # print(f"Valid sum found: {valid_sum}")
            if not valid_sum:
                solution = numbers[end + 1]
                break
            start += 1
            end += 1

        print(f"Solution: {solution}")
        return end + 1, solution

    def solve_part2(self):
        numbers = [int(d) for d in self.raw_data]
        part1_idx, part1_number = self.solve_part1()
        print(f"idx: {part1_idx}, value: {part1_number}")

        for start in range(0, part1_idx):
            sum = 0
            for end in range(start, part1_idx):
                sum += numbers[end]
                if sum == part1_number:
                    the_range = numbers[start : end + 1]
                    print(f"Range: {the_range}")
                    the_range.sort()
                    print(f"Range Sorted: {the_range}")

                    print(
                        f"Range adds to {sum}: {start}:{end+1}, values: {the_range[0]}, {the_range[-1]}, Sum: {the_range[0]+the_range[-1]}"
                    )

    def find_sum(self, numbers, value):
        # print(f"Searching {numbers} for sum of {value}...")
        for idx1, x in enumerate(numbers):
            for idx2, y in enumerate(numbers):
                if idx1 == idx2:
                    continue
                # print(f"({idx1, idx2}) is {x}+{y}, sum = {x+y}")
                if x + y == value:
                    # print(f"Found: {x} + {y}  ({idx1}, {idx2})")
                    return (idx1, idx2)

        return None
