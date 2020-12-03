from day01 import day01
from day02 import day02
from day03 import day03
from fileutils import file_as_list


def main():
    day = "03"
    data = file_as_list(f"day{day}/day{day}input.txt")

    runner = day03.Day03(data)

    print("Part 1")
    runner.solve_part1()

    print("Part 2")
    runner.solve_part2()


if __name__ == "__main__":
    main()
