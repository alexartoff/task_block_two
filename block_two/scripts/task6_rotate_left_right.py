#!/usr/bin/env python


def rotated_left(lst):
    if lst:
        out = lst[1:] + lst[:1]
    return out


def rotated_right(lst):
    if lst:
        out = lst[-1:None] + lst[None:(len(lst) - 1)]
    return out


def main():
    l = [1, 2, 3, 4, 5]
    ll = 'abcde'
    res_left = rotated_left(ll)
    res_right = rotated_right(ll)


if __name__ == "__main__":
    main()
