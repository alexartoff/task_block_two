#!/usr/bin/env python


def hamming_weight(num):
    num_bin_str = str(bin(num))
    count = 0
    for i in num_bin_str[1:]:
        if i == "1":
            count += 1
    return count


def main():
    print(hamming_weight(0))


if __name__ == "__main__":
    main()
