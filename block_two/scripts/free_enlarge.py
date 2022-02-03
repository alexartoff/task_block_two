#!/usr/bin/env python


def enlarge(frame):
    double = []
    for r in range(len(frame)):
        txt = ''
        for c in range(len(frame[r])):
            txt += 2* frame[r][c]
        double.append(txt)
        double.append(txt)
    return double


def main():
    frame = [
        '# #',
        ' # ',
        '# #',
    ]
    frame_a = [' ']
    frame_b = [
        ' *',
        '# ',
    ]
    frame_o = []
    print(enlarge(frame))
    print(enlarge(frame_a))
    print(enlarge(frame_b))
    print(enlarge(frame_o))


if __name__ == "__main__":
    main()
