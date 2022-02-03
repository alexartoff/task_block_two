#!/usr/bin/env python

# 0:           1
# 1:          1 1
# 2:        1  2  1
# 3:       1 3   3 1
# 4:      1 4  6  4 1
# 5:     1 5 10 10 5 1


def triangle(num):
    output = [1]
    for i in range(1, num + 1):
        if i == 1:
            output = [1, 1]
        elif i > 1:
            ext = []
            for j in range(1, i):
                ext.append(output[j - 1] + output[j])
            output = output[:1] + ext + output[-1:]
    return output


def main():
    print(triangle(10))


if __name__ == "__main__":
    main()
