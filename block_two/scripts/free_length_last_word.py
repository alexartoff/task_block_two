#!/usr/bin/env python


def length_of_last_word(frame):
    output = 0
    filter = ['\\n', '\\t']
    filtered = ''
    for char in frame:
        if char != filter[0] or char != filter[1]:
            filtered += char
        else:
            filtered += ' '
    # print(filtered.rstrip())
    splitted = filtered.rstrip().split()
    if splitted:
        output = len(splitted[-1])
        print(splitted[-1])
    return output


def main():
    frame = '   qwerty\n\t '
    print(length_of_last_word(frame))


if __name__ == "__main__":
    main()
