class BusSchedule:
    def __init__(self, data):
        self.earliest = int(data[0])
        self.buses = data[1].split(',')

    def get_active_buses(self):
        return [int(b) for b in self.buses if b != 'x']

    def get_constraints(self):
        result = []
        for i, b in enumerate(self.buses):
            if b != 'x':
                result.append((int(b), i))
        return result
