class Day13:
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        earliest = int(self.raw_data[0])
        buses = self.raw_data[1].split(',')

        best_bus = None
        min_wait = None
        for b in buses:
            if b == 'x':
                continue
            bus_id = int(b)
            wait = bus_id - (earliest % bus_id)
            if wait == bus_id:
                wait = 0
            print(f"Bus {bus_id}: wait {wait}")
            if min_wait is None or wait < min_wait:
                min_wait = wait
                best_bus = bus_id

        print(f"Best bus: {best_bus}, wait: {min_wait}, answer: {best_bus * min_wait}")

    def solve_part2(self):
        buses = self.raw_data[1].split(',')
        constraints = []
        for i, b in enumerate(buses):
            if b != 'x':
                constraints.append((int(b), i))

        print(f"Solving for {len(constraints)} bus constraints")

        t = 0
        step = 1
        for n, offset in constraints:
            while (t + offset) % n != 0:
                t += step
            step *= n  # works because all AoC bus IDs are coprime

        print(f"Earliest timestamp: {t}")
