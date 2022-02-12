#!/usr/bin/env python


def sum_of_intervals(arr):
    output = 0
    if len(arr) == 1:
        output += arr[0][1] - arr[0][0]
    else: #len > 1
        lst = sorted(arr)
        tmp = 0
        for i in lst:
            if lst.index(i) == 0:
                tmp = i[1] - i[0]
                print('0', i, 'первый элемент', tmp)
            else: 
                count = lst.index(i)
                # когда текущий больше предыдущего и по 0 и по 1 и не пересекаются
                # текущий не пересекается с предыдущим
                if i[0] > lst[count - 1][0] \
                   and i[1] > lst[count - 1][1] \
                   and i[0] > lst[count - 1][1]:
                    tmp += i[1] - i[0]
                    print(count, i, 'не пересекается с', lst[count - 1], tmp)
                # когда текущий больше предыдущего и по 0 и по 1, но они пересекаются
                # текущий пересекается с предыдущим
                if i[0] > lst[count - 1][0] \
                   and i[1] > lst[count - 1][1] \
                   and i[0] < lst[count - 1][1]:
                    tmp += i[1] - lst[count - 1][1]
                    print(count, i, 'пересекается с', lst[count - 1], tmp)
                # когда текущий 0 равен предыдущему 0 и текущий 1 больше предыдущего 1
                # текущий длинее предыдущего диапазона
                elif i[0] == lst[count - 1][0] \
                     and i[1] > lst[count - 1][1]:
                    tmp += i[1] - i[0] - (lst[count - 1][1] - lst[count - 1][0])
                    print(count, i, 'длинее предыдущего', tmp)
                # когда текущий 0 больше предыдущего 0 и текущий 1 мешьше предыдущиго 1
                # текущий внутри предыдущего диапазона
                elif i[0] > lst[count - 1][0] \
                     and i[1] < lst[count - 1][1]:
                    lst[count] = lst[count - 1]
                #     tmp += 0
                    print(count, i, 'внутри предыдущего', lst[count], tmp)
            output = tmp
    return output


def sum_of_intervals_t(intervals):
    values = []
    for start, end in intervals:
        print(f"[{start}, {end}]")
        for i in range(start, end):
            if i not in values:
                values.append(i)
        print(sorted(values))
    return len(values)


def main():
    arr = [
        [1, 11],
        [50, 100],
        [60, 70],
        [90, 120],
        [100, 110]
    ]
    print(sum_of_intervals(arr))
    print(sum_of_intervals_t(arr))


if __name__ == "__main__":
    main()
