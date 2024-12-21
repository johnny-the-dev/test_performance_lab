from sys import argv
import math


def get_circle_data() -> tuple:
    with open(argv[1]) as file:
        x, y = map(int, file.readline().split())
        radius = int(file.readline())

    return x, y, radius


def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def print_result(distance: float, radius: int) -> None:
    if distance < radius:
        print(1)
    elif distance > radius:
        print(2)
    else:
        print(0)


def main() -> None:
    if len(argv) != 3:
        print(
            'Error: incorrect number of arguments',
            'Usage: python task2.py <circle_data_file> <dots_coords_file>',
            sep='\n'
        )
        return

    circle_x, circle_y, radius = get_circle_data()

    with open(argv[2]) as dots_file:
        for line in dots_file:
            dot_x, dot_y = map(int, line.split())
            distance = calculate_distance(circle_x, circle_y, dot_x, dot_y)
            print_result(distance, radius)


if __name__ == '__main__':
    main()
