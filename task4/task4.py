from sys import argv
import math


def main() -> None:
    if len(argv) < 2:
        print(
            'Error: not enough arguments',
            'Usage: python task3.py <nums_file>',
            sep='\n'
        )
        return

    with open(argv[1]) as file:
        nums = list(map(int, file.readlines()))

    total_sum = sum(nums)

    total_difference = sum(abs(total_sum - number * len(nums)) for number in nums)
    steps_required = math.ceil(total_difference / len(nums))

    print(steps_required)


if __name__ == '__main__':
    main()
