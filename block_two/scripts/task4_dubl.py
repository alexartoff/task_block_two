#!/usr/bin/env python


def duplicate(lst):
    for i in range(0, len(lst)):
        lst.append(lst[i])


def main():
    l = [1, 2, 3, 4, 5]
    duplicate(l)
    print(l)


if __name__ == "__main__":
    main()
