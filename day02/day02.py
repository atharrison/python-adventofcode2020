import re


class Day02:
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        total = 0
        structured = self.process_raw()
        for item in structured:
            match_count = len(re.findall(item[2], item[3]))
            if match_count >= item[0] and match_count <= item[1]:
                total += 1

        print(f"Solution: {total}")

    def solve_part2(self):
        total = 0
        structured = self.process_raw()
        for item in structured:
            password = item[3]
            idx1 = item[0] - 1
            idx2 = item[1] - 1
            try:
                if password[idx1] == item[2]:
                    # one match:
                    if len(password) < idx2 or password[idx2] != item[2]:
                        total += 1
                elif len(password) >= idx2 and password[idx2] == item[2]:
                    total += 1

            except Exception:
                pass

        print(f"Solution: {total}")

    def process_raw(self):

        items = []
        for line in self.raw_data:
            # 17-19 p: pwpzpfbrcpppjppbmppp
            split1 = line.split(":", 2)
            split2 = split1[0].split("-", 2)
            split3 = split2[1].split(" ", 2)

            items.append((int(split2[0]), int(split3[0]), split3[1], split1[1].strip()))

        return items
