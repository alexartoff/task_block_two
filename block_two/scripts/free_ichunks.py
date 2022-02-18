#!/usr/bin/env python


from typing import Iterable
from itertools import count, islice


def ichunks(chunk, flow):
    output = []
    if isinstance(flow, Iterable):
        stop_iter = 3
        stream = iter(flow)
        t = zip(*[stream] * chunk)
        lst = [[]]
        while stop_iter != 0:
            try:
                tmp = list(next(t))
                lst.append(tmp)
                stop_iter -= 1
            except StopIteration:
                break
        lst.pop(0)
        output = list(islice(lst, 100))
    return output


def ichunks_t(size, source):
    return map(list, zip(*([iter(source)] * size)))
    # "iter(source)" получает именно итератор, даже если на вход
    # был передан iterable (строка, список).
    #
    # "[iterator] * n" размножает ссылки на итератор.
    #
    # "zip(*l)" пакует в кортежи все первые элементы из
    # списка источников "l", затем все вторые, и так далее.
    # Так как все источники для zip, это ссылки на один и тот же
    # итератор, при переходе от ссылки к ссылке курсор передвигается
    # всё дальше. Поэтому кортежи содержат последовательные элементы.
# END


def main():
    strm = count(1000, 3)
    print(ichunks(1, [4, 5, 6]))
    print(ichunks(1, strm))
    print(ichunks(3, strm))


if __name__ == "__main__":
    main()
