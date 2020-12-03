class Day03:
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        grid = self.load_grid()
        x = 3
        y = 1
        size = len(grid[0])
        height = len(grid)
        print(grid, size, height)

        trees = 0
        while y < height:
            if grid[y][x] == "#":
                trees += 1
            y += 1
            x += 3
            if x >= size:
                x = x - size
        print(trees)

    def solve_part2(self):
        grid = self.load_grid()
        x = 3
        y = 1
        size = len(grid[0])
        height = len(grid)

        tree_hits = []
        for slopes in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
            trees = 0
            x = slopes[0]
            y = slopes[1]
            while y < height:
                if grid[y][x] == "#":
                    trees += 1
                y += slopes[1]
                x += slopes[0]
                if x >= size:
                    x = x - size
            print(trees)
            tree_hits.append(trees)

        prod = 1
        for t in tree_hits:
            prod *= t

        print(prod)

    def load_grid(self):

        grid = []
        for line in self.raw_data:
            grid.append(list(line))

        return grid
