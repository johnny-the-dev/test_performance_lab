def main() -> None:
    n, m = map(int, input().split())

    if n == 1:
        print(1)

    nums = range(1, n + 1)
    index_start = 0
    num_path = ''

    while True:
        num_path += str(nums[index_start])
        index_start = (index_start + m) % n - 1

        if index_start == 0:
            break

    print(num_path)


if __name__ == '__main__':
    main()
