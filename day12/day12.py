import copy


class Day12:
    # started 1:45 after
    def __init__(self, data):
        self.raw_data = data
        self.max_x = 0
        self.max_y = 0
        self.part2 = False
        self.max_per_seat = 4

    def solve_part1(self):
        x = 0
        y = 0
        dir_x = 1
        dir_y = 0
        for line in self.raw_data:
            print(line)
            magnitude = int(line[1:])
            d = line[0]
            print(f"line -> {d}:{magnitude}")
            if d == "F":
                x += dir_x * magnitude
                y += dir_y * magnitude

            if d == "L":
                dir_x, dir_y = self.rotate_counterclockwise(dir_x, dir_y, magnitude)
            if d == "R":
                dir_x, dir_y = self.rotate_clockwise(dir_x, dir_y, magnitude)

            if d == "E":
                x += magnitude
            if d == "W":
                x -= magnitude
            if d == "N":
                y += magnitude
            if d == "S":
                y -= magnitude
            print(
                f"Moved to {x, y} using {d} and {magnitude}. Boat Vector {dir_x, dir_y}"
            )

        print(f"Final x,y: {x, y}. Distance: {abs(x)+abs(y)}")

    def rotate_clockwise(self, x, y, degrees):
        if degrees == 180:
            return -x, -y

        num_rotations = degrees // 90
        for _ in range(num_rotations):
            x, y = self.rotate_90_clockwise(x, y)

        return x, y

    def rotate_counterclockwise(self, x, y, degrees):
        """
        0 == 0
        90 == 270
        180 == 180
        270 == 90
        """
        if degrees == 180:
            return -x, -y
        if degrees == 90:
            return self.rotate_clockwise(x, y, 270)
        if degrees == 270:
            return self.rotate_clockwise(x, y, 90)

    def rotate_90_clockwise(self, x, y):
        # Should use matrix multiplication, but :shrug:
        if x == 0:
            if y == 1:
                return 1, 0
            else:
                return -1, 0

        if x == 1:
            return 0, -1
        else:
            return 0, 1

    def solve_part2(self):
        x = 0
        y = 0
        # dir_x = 1
        # dir_y = 0
        mag_x = 10
        mag_y = 1

        for line in self.raw_data:
            print(line)
            magnitude = int(line[1:])
            d = line[0]
            print(f"line -> {d}:{magnitude}")
            if d == "F":
                movecount = magnitude
                print(f"Forward moving dist {mag_x, mag_y} {movecount} times")
                for m in range(movecount):
                    x += mag_x
                    y += mag_y

            # Convert counter-clockwise to clockwise rotation
            if d == "L":
                d = "R"
                if magnitude == 90:
                    magnitude = 270
                elif magnitude == 270:
                    magnitude = 90

            if d == "R":
                if magnitude == 180:
                    # Swap both signs and magnitudes
                    (mag_x, mag_y) = (-mag_x, -mag_y)
                else:
                    num_rotations = magnitude // 90
                    for _ in range(num_rotations):
                        mag_x, mag_y = self.rotate_magnitutes_90_clockwise(mag_x, mag_y)

            if d == "E":
                mag_x += magnitude
            if d == "W":
                mag_x -= magnitude
            if d == "N":
                mag_y += magnitude
            if d == "S":
                mag_y -= magnitude
            print(
                f"Moved to {x, y} using {d} and {magnitude}. Waypoint dist {mag_x, mag_y}"
            )

        print(f"Final x,y: {x, y}. Distance: {abs(x)+abs(y)}")

    def rotate_magnitutes_90_clockwise(self, x, y):
        # import pdb

        # pdb.set_trace()
        if x > 0:
            if y > 0:
                return y, -x
            elif y < 0:
                return y, -x
            else:
                return 0, -x
        elif x < 0:
            if y > 0:
                return y, -x
            if y < 0:
                return y, -x
            else:
                return 0, -x
        else:
            if y > 0:
                return -y, 0
            if y < 0:
                return -y, 0
            else:
                return 0, 0
