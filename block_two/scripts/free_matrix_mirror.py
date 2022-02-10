#!/usr/bin/env python


def mirror_matrix(arr):
    if len(arr) <= 1:
        return None
    else:
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                if c > len(arr[r]) // 2 - 1:
                    arr[r][c] = arr[r][len(arr[r]) - c - 1]
    # print(arr)


def main():
    arr_one = [
        [10, 20, 30, 40],
        [60, 70, 80, 90]
    ]
    arr_two = [
        ['aa', 'bb', 'cc'],
        ['11', '22', '33'],
    ]
    arr_three = []
    arr_four = [[1]]

    print(mirror_matrix(arr_one))
    print(mirror_matrix(arr_two))
    print(mirror_matrix(arr_three))
    print(mirror_matrix(arr_four))


if __name__ == "__main__":
    main()
