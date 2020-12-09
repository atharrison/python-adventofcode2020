from day01 import day01
from day02 import day02
from day03 import day03
from day04 import day04
from day05 import day05
from day06 import day06
from day07 import day07
from day08 import day08
from day09 import day09
from fileutils import file_as_list


def main():
    day = "09"
    data = file_as_list(f"day{day}/day{day}input.txt")
    # data = file_as_list(f"day{day}/day{day}input_sample.txt")
    # data = file_as_list(f"day{day}/day{day}input_sample2.txt")

    runner = day09.Day09(data)

    print("Part 1")
    runner.solve_part1()

    print("Part 2")
    runner.solve_part2()


if __name__ == "__main__":
    main()
