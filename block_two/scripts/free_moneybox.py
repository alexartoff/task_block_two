#!/usr/bin/env python

from typing import Counter


def visualize(data, bar_char = '₽'):
    lst = list(data)
    lst.sort()
    double_bar_char = 2 * bar_char
    cnt = dict(Counter(lst))
    # dct = cnt.elements
    # print(cnt, lst, double_bar_char)
    out_str = build_mtrx(cnt, double_bar_char)
    return out_str


def build_mtrx(dct, dbc):
    lst = []
    max_len = get_max(dct)
    count = 0
    for key in dct:
        lst.append([])
        if key < 10:
            lst[count].append(f"{key}  ")
        else:
            lst[count].append(f"{key} ")
        lst[count].append("---")
        for _ in range(dct[key]):
            lst[count].append(f"{dbc} ")
        for i in range(max_len + 1):
            if i == dct[key]:
                lst[count].append(f"{dct[key]}  ")
            elif i > dct[key]:
                lst[count].append("   ")
        count += 1
    lst_rtd = transposed(lst)
    # print(lst_rtd)
    out_str = make_str_from_list(lst_rtd)
    return out_str


def make_str_from_list(lst):
    outstr = ''
    lst.reverse()
    count = 0
    for l in lst:
        # print(count, l, len(lst))
        line = ''.join(map(str, l))
        if count == (len(lst) - 1):
            outstr += line[:-1]
        else:
            outstr += line[:-1] + '\n'
        # print(line[:-1])
        count += 1
    return outstr


def get_max(dct):
    max_len = 0
    for key in dct:
        if max_len <= dct[key]:
            max_len = dct[key]
    return max_len


def transposed(arr):
    trans = []
    for i in range(len(arr[0])):
        trans.append([])
        for j in range(len(arr)):
            trans[i].append(arr[j][i])
    return trans


def main():
    money = (10, 5, 5, 5, 1, 2, 5, 1, 10, 20, 20, 20)
    print(visualize(money))
    print(visualize(money, bar_char='$'))


if __name__ == "__main__":
    main()
