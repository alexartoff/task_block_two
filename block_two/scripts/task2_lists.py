#!/usr/bin/env python
# from math import sqrt
import math


def get_square_roots(num):
    if num < 0:
        return []
    elif num == 0:
        return[0]
    else:
        output = []
        output.append(-math.sqrt(num))
        output.append(math.sqrt(num))
        return output


def get_range(num):
    count = 0
    output = []
    if num <= 0:
        return []
    else:
        while count < num:
            output.append(count)
            count += 1
        return output


def main():
    print(get_square_roots(5))
    print(get_range(10))


if __name__ == "__main__":
    main()
