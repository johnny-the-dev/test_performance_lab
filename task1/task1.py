def main() -> None:
    num_digits, step_length = map(int, input().split())

    # if step_length <= 0:
    #     print('The step length must be a positive number.')
    #     return

    if num_digits == 1:
        print(1)
        return

    digits = list(range(1, num_digits + 1))
    path = str(digits[0])
    current_index = step_length % num_digits - 1

    while current_index != 0:
        path += str(digits[current_index])
        current_index = (current_index + step_length) % num_digits - 1

    print(path)


if __name__ == '__main__':
    main()
