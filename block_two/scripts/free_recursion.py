#!/usr/bin/env python


def recurs(arr):
    output = []
    for i in arr:
        if isinstance(i, list):
            output += recurs(i)
            # print(i, output)
        else:
            output.append(i)
            # print(i, output)
    return output


def main():
    arr = [1, [], [2, 3, [4, 5]], 6]
    print(arr, recurs(arr))


if __name__ == "__main__":
    main()
