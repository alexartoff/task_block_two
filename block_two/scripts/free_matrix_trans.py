#!/usr/bin/env python


def transposed(arr):
    output = []
    for i in range(len(arr[0])):
        output.append([])
        for j in range(len(arr)):
            output[i].append(arr[j][i])
    return output


def main():
    arr_one = [
        [10, 20],
        [30, 40]
    ]
    arr_two = [
        [1, 2, 3]
    ]
    arr_three = [
        [1],
        [2],
        [3]
    ]

    print(transposed(arr_one))
    print(transposed(arr_two))
    print(transposed(arr_three))


if __name__ == "__main__":
    main()
