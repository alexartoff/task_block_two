#!/usr/bin/env python


def rotate(lst):
    if lst:
        lst.insert(0, lst.pop())


def main():
    l = [1, 2, 3, 4, 5]
    res = rotate(l)
    print("result:", res)
    ll = []
    resres = rotate(ll)
    print("result:", resres)


if __name__ == "__main__":
    main()
