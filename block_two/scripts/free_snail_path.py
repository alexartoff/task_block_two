#!/usr/bin/env python


def rotate(mtrx):
    output = [list(i) for i in zip(*mtrx)]
    return output


def snail_path(mtrx):
    lst = []
    dir = {'right': 1, 'bottom': 2, 'left': 3, 'up': 4}
    counter = 1
    while len(mtrx) != 0:
        if counter == dir['right']:
            to_lst = mtrx.pop(0)
        elif counter == dir['bottom']:
            to_lst = mtrx.pop(-1)
        elif counter == dir['left']:
            to_lst = reversed(mtrx.pop(-1))
        elif counter == dir['up']:
            to_lst = reversed(mtrx.pop(0))
        lst.extend(to_lst)
        counter += 1
        mtrx = rotate(mtrx)
        if counter > 4:
            counter = 1
    return lst


def main():
    arr_one = [
        [1],
        [2],
        [3],
        [4]
    ]
    arr_two = [
        ['aa', 'bb', 'cc', 'dd'],
        ['11', 777, [0], None],
        ['zz', True, False, []],
        ['*', {}, 99, object],
    ]
    arr_three = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    arr_four = [
        [1, 2],
        [3, 4]
    ]

    arr_fifth = [
        [None, 0, True],
        [-1, '', False],
        [[], 'foo', object],
    ]

    print('1', snail_path(arr_one))
    print('2', snail_path(arr_two))
    print('3', snail_path(arr_three))
    print('4', snail_path(arr_four))
    print('5', snail_path(arr_fifth))


if __name__ == "__main__":
    main()
