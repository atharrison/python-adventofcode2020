from day13.schedule import BusSchedule


class Day13:
    def __init__(self, data):
        self.schedule = BusSchedule(data)

    def solve_part1(self):
        earliest = self.schedule.earliest
        best_bus = None
        min_wait = None
        for bus_id in self.schedule.get_active_buses():
            wait = bus_id - (earliest % bus_id)
            if wait == bus_id:
                wait = 0
            print(f"Bus {bus_id}: wait {wait}")
            if min_wait is None or wait < min_wait:
                min_wait = wait
                best_bus = bus_id

        print(f"Best bus: {best_bus}, wait: {min_wait}, answer: {best_bus * min_wait}")

    def solve_part2(self):
        constraints = self.schedule.get_constraints()
        print(f"Solving for {len(constraints)} bus constraints")

        t = 0
        step = 1
        for n, offset in constraints:
            while (t + offset) % n != 0:
                t += step
            step *= n  # works because all AoC bus IDs are coprime

        print(f"Earliest timestamp: {t}")
