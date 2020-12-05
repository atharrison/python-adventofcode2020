import re


class Day05:
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        largest = 0
        for item in self.raw_data:
            seat_id = self.calculate_seat_id(item)
            if seat_id > largest:
                largest = seat_id
        print(f"Largest ID: {largest}")

    def solve_part2(self):
        claimed = []
        for item in self.raw_data:
            claimed.append(self.calculate_seat_id(item))

        claimed.sort()
        seat = -1
        for s in claimed:
            print(s)
        for idx, s in enumerate(claimed):
            print(f"Seat {s} idx{idx} next to seat {claimed[idx+1]}")
            if s + 1 != claimed[idx + 1]:
                print("Found it! " + str(s + 1))
                return

    def calculate_seat_id(self, item):
        partitions = [int(i) for i in self.normalize_partitions(item)]

        row_partitions = partitions[0:7]
        seat_partitions = partitions[7:10]
        print(str(partitions))
        print(str(row_partitions) + ":" + str(seat_partitions))

        row = self.binary_partition(row_partitions)
        seat = self.binary_partition(seat_partitions)

        seat_id = row * 8 + seat
        # print(f"{row} * 8 + {seat} = {seat_id}")
        return int(seat_id)

    def normalize_partitions(self, str):
        return (
            str.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        )

    def binary_partition(self, data):
        size = 2 ** len(data)

        high = size
        low = 1
        for d in data:

            diff = high - low + 1
            # print(f"[{low} - {high}] next diff: {diff}")
            if diff == 2:
                if d:
                    return high - 1
                else:
                    return low - 1
            if d:

                low = low + diff // 2
            else:
                high = high - diff // 2
