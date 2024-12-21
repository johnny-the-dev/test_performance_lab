def normalize_step(step: int) -> int:
    if step > 0:
        return step - 1
    if step < 0:
        return step + 1
    return 0


def main() -> None:
    num_digits, step = map(int, input().split())

    step_normalized = normalize_step(step)
    current_index = step_normalized % num_digits
    path = '1'

    while current_index != 0:
        path += str(current_index + 1)
        current_index = (current_index + step_normalized) % num_digits

    print(path)


if __name__ == '__main__':
    main()
