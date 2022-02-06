#!/usr/bin/env python


def compare_version(a, b):
    a_arr = a.split('.')
    b_arr = b.split('.')
    print(a_arr, b_arr)
    if int(a_arr[0]) > int(b_arr[0]):
        return 1
    elif int(a_arr[0]) == int(b_arr[0]):
        if int(a_arr[1]) > int(b_arr[1]):
            return 1
        elif int(a_arr[1]) < int(b_arr[1]):
            return -1
        else:
            return 0
    else:
        return -1


def main():
    vers = '0.2', '0.12'
    print(compare_version(vers[0], vers[1]))


if __name__ == "__main__":
    main()
