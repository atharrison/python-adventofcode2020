from day01 import day01
from day02 import day02
from fileutils import file_as_list


def main():
    day = "02"
    data = file_as_list(f"day{day}/day{day}input.txt")

    runner = day02.Day02(data)
    runner.solve_part1()


if __name__ == "__main__":
    main()
