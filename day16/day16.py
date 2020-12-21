import copy
import re


class Day16:

    # started 0:02 after
    def __init__(self, data):
        self.raw_data = data
        self.ticket_types = {}
        self.your_ticket = ""
        self.nearby_tickets = []
        self.valid_tickets = []

        self.valid_chart = {}
        self.load_data()

    def solve_part1(self):
        # print(self.ticket_types)
        # print(self.your_ticket)
        # print(self.nearby_tickets)

        invalid_sum = 0
        for t in self.nearby_tickets:
            for n in t:
                if not self.valid_number(n):
                    invalid_sum += n

        print(f"Scanning Error Rate: {invalid_sum}")

    def valid_number(self, num):
        for _, ticket_type_ranges in self.ticket_types.items():
            for r in ticket_type_ranges:
                if num >= r[0] and num <= r[1]:
                    return True
        return False

    def solve_part2(self):
        for t in self.ticket_types.keys():
            self.valid_chart[t] = [1] * len(self.your_ticket)

        for t in self.nearby_tickets:
            valid = True
            for n in t:
                if not self.valid_number(n):
                    valid = False
            if valid:
                self.valid_tickets.append(t)

        print(
            f"Nearby Tickets: {len(self.nearby_tickets)}, Valid: {len(self.valid_tickets)}"
        )

        # Also append our ticket:
        self.valid_tickets.append(self.your_ticket)

        for t in self.valid_tickets:
            for col, n in enumerate(t):
                mapping = self.valid_for(n)

                for tt, valid in mapping.items():
                    if valid == 0:
                        self.valid_chart[tt][col] = 0
                print(f"Ticket {t} column {col}={n} Mapping: {mapping}")

        print(f"Valid chart: {self.valid_chart}")

        col_to_type_mapping = {}
        current_chart = copy.deepcopy(self.valid_chart)

        while len(current_chart) > 0:
            # print(f"Current chart: {current_chart}")
            next_type, next_col = self.find_next_unique_match(current_chart)
            col_to_type_mapping[next_type] = next_col
            # Clear chart of used column:
            for _, mapping in current_chart.items():
                mapping[next_col] = 0

            print(f"{next_type} => {next_col}")
            del current_chart[next_type]

        print(f"Mapping: {col_to_type_mapping}")
        values = 1
        for tt, col in col_to_type_mapping.items():
            if tt.startswith("departure"):
                your_ticket_value = self.your_ticket[col]
                print(
                    f"{tt} = {col}, {your_ticket_value} x {values} = {values * your_ticket_value}"
                )
                values *= your_ticket_value

        print(f"Departure multiplicated: {values}")

    def find_next_unique_match(self, chart):
        for tt, mapping in chart.items():
            if sum(mapping) == 1:
                col = mapping.index(1)
                return tt, col
        print(f"COULD NOT FIND UNIQUE MATCH! Chart: {chart}")

    # def merge_mapping(self, m1, m2):
    #     merged = {}
    #     for k in m1:
    #         merged[k] = m1[k] * m2[k]

    def valid_for(self, num):
        mapping = self.make_mapping()
        for tt, ticket_type_ranges in self.ticket_types.items():
            valid = False
            for r in ticket_type_ranges:
                if num >= r[0] and num <= r[1]:
                    valid = True
            if not valid:
                mapping[tt] = 0
        return mapping

    def make_mapping(self):
        mapping = {}
        for tt in self.ticket_types.keys():
            mapping[tt] = 1
        return mapping

    def load_data(self):
        section = 0

        for line in self.raw_data:
            if line == "":
                continue
            elif line == "your ticket:":
                section = 1
                continue
            elif line == "nearby tickets:":
                section = 2
                continue

            print(f"S{section} {line}")
            if section == 0:
                self.add_ticket_type(line)
            elif section == 1:
                self.add_your_ticket(line)
            elif section == 2:
                self.add_nearby_ticket(line)

    def add_your_ticket(self, line):
        """
        your ticket:
        7,1,14
        """
        self.your_ticket = [int(d) for d in line.split(",")]

    def add_nearby_ticket(self, line):

        """
        nearby tickets:
        7,3,47
        40,4,50
        55,2,20
        38,6,12
        """
        self.nearby_tickets.append([int(d) for d in line.split(",")])

    def add_ticket_type(self, line):
        ticket_type_pattern = re.compile(r"^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")
        """
        class: 1-3 or 5-7
        row: 6-11 or 33-44
        seat: 13-40 or 45-50
        """
        ticket_data = ticket_type_pattern.match(line)
        self.ticket_types[ticket_data[1]] = (
            (int(ticket_data[2]), int(ticket_data[3])),
            (int(ticket_data[4]), int(ticket_data[5])),
        )
