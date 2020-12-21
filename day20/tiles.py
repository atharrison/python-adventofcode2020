class Tile:
    def __init__(self, num):
        self.num = num
        self.matrix = []

    def add_line(self, line):
        self.matrix.append(list(line))

    def __str__(self):
        return f"{self.matrix}"

    def __repr__(self):
        return self.__str__()
