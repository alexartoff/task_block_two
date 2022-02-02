#!/usr/bin/env python


def find_index(txt, source):
    for (index, _) in enumerate(source):
        if source[index] == txt:
            return index
    else:
        return None


def main():
    out = find_index(4, [1, 2, 3, 4, 5, 6, 7, 4])
    if out is None:
        print(True)
    else:
        print(out)


if __name__ == "__main__":
    main()
