import copy


class Day11:
    def __init__(self, data):
        self.raw_data = data
        self.max_x = 0
        self.max_y = 0
        self.part2 = False
        self.max_per_seat = 4

    def solve_part1(self):
        self.load_grid()

        print(f"GRID: max_x/max_y: {self.max_x},{self.max_y}")

        previous_grid = copy.deepcopy(self.grid)
        next_grid = self.change_grid(previous_grid)
        count = 0
        while not self.compare_grids(next_grid, previous_grid):
            # self.print_grid(next_grid)
            count += 1
            previous_grid = copy.deepcopy(next_grid)
            next_grid = self.change_grid(previous_grid)

        print(f"Cycle after {count}")
        seats_filled = self.count_seats(next_grid)
        print(f"Filled Seats: {seats_filled}")

    def count_seats(self, grid):
        count = 0
        for line in grid:
            for s in line:
                if s == "#":
                    count += 1
        return count

    def print_grid(self, grid):
        for line in grid:
            print(line)
        print("-----")

    def compare_grids(self, grid1, grid2):
        return grid1 == grid2
        # for idx, line in enumerate(grid1):
        #     if line != grid2[idx]:
        #         return False
        # return True

    def change_grid(self, current_grid):

        new_grid = []
        for y in range(len(current_grid)):
            row = []
            for x in range(len(current_grid[0])):
                row.append(self.change_seats(x, y, current_grid))
            new_grid.append(row)
        return new_grid

    def change_seats(self, x, y, current_grid):
        if current_grid[y][x] == ".":
            # print(f"Floor at {x},{y}")
            return "."
        elif current_grid[y][x] == "L":
            if self.passengers_adjacent(x, y, current_grid) == 0:
                # print(f"NO # near {x},{y}, filling seat.")
                return "#"
        elif current_grid[y][x] == "#":
            if self.passengers_adjacent(x, y, current_grid) >= self.max_per_seat:
                # print(f"FULL at {x},{y}, vacating seat.")
                return "L"

        return current_grid[y][x]

    def passengers_adjacent(self, x, y, current_grid):
        if self.part2:
            return self.passengers_adjacent_part2(x, y, current_grid)
        else:
            return self.passengers_adjacent_part1(x, y, current_grid)

    def passengers_adjacent_part1(self, x, y, current_grid):
        passengers = 0
        for jj in [y - 1, y, y + 1]:
            for ii in [x - 1, x, x + 1]:
                if ii == x and jj == y:
                    continue
                # if ii >= 0 and ii < self.max_x and jj >= 0 and jj < self.max_y:
                if self.in_grid(ii, jj):
                    # print(f"Near {x},{y}, found {current_grid[jj][ii]} at {ii},{jj}")
                    if current_grid[jj][ii] == "#":
                        # print(f"Passenger near {x},{y} at {ii},{jj}")
                        passengers += 1
        # if passengers > 3:
        # print(f"Found {passengers} near {x}, {y}")
        return passengers

    def in_grid(self, x, y):
        return x >= 0 and x < self.max_x and y >= 0 and y < self.max_y

    def passengers_adjacent_part2(self, x, y, current_grid):
        passengers = 0
        for jj in [y - 1, y, y + 1]:
            for ii in [x - 1, x, x + 1]:
                if ii == x and jj == y:
                    continue
                if self.passenger_in_vector(x, y, ii, jj, current_grid):
                    passengers += 1
        # if passengers >= self.max_per_seat:
        #     print(f"Too many visible from {x},{y}.")
        return passengers

    def passenger_in_vector(self, x, y, ii, jj, current_grid):
        dir_x = ii - x
        dir_y = jj - y
        while self.in_grid(ii, jj):
            # print(f"At {x},{y} -> {dir_x},{dir_y} checking {ii},{jj} ")
            if current_grid[jj][ii] == "#":
                # print(f"At {x},{y} -> {dir_x},{dir_y} Found passenger at {ii},{jj} ")
                return True
            elif current_grid[jj][ii] == "L":
                return False
            ii += dir_x
            jj += dir_y

        return False

    def load_grid(self):
        self.grid = []
        # print(self.raw_data)
        for line in self.raw_data:
            # print(list(line))
            self.grid.append(list(line))

        self.max_x = len(self.grid[0])
        self.max_y = len(self.grid)

    def solve_part2(self):
        self.part2 = True
        self.max_per_seat = 5
        self.solve_part1()
