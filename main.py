from day01 import day01
from fileutils import file_as_list


def main():
    data = file_as_list("day01/day01input.txt")

    runner = day01.Day01(data)
    runner.solve_part2()


if __name__ == "__main__":
    main()
