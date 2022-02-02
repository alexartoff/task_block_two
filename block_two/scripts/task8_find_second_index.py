#!/usr/bin/env python
from block_two.scripts.task7_find_index import find_index as fi


def find_second_index(txt, source):
    cursor = iter(source)
    first = fi(txt, source)
    # print("first", first, source[first:])
    for (index, i) in enumerate(cursor):
        if index > first and i == txt:
            return index
    else:
        return None


def main():
    source = "banana"
    print(find_second_index("n", source))


if __name__ == "__main__":
    main()
