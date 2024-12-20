from sys import argv
import math


def main() -> None:

    if len(argv) < 3:
        print(
            'Error: not enough arguments',
            'Usage: python task2.py <circle_data_file> <dots_coords_file>',
            sep='\n'
        )
        return

    with open(argv[1]) as file:
        x, y = map(int, file.readline().split())
        radius = int(file.readline())

    with open(argv[2]) as file:
        line = file.readline().strip()

        while line:
            x_test, y_test = map(int, line.split())
            distance = math.sqrt((x_test - x)**2 + (y_test - y)**2)

            if distance < radius:
                print(1)
            elif distance > radius:
                print(2)
            else:
                print(0)

            line = file.readline().strip()


if __name__ == '__main__':
    main()
