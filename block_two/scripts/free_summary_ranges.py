#!/usr/bin/env python


def summary_ranges(arr):
    output = []
    if len(arr) > 1:
        strt, stp, dif, cnt = 0, 0, 0, 0
        cur_dif = 0
        for i in range(1, len(arr)):
            dif = arr[i] - arr[i - 1]
            if dif == 1 and cnt == 0:
                # print('!!! write start for i=', i)
                strt = str(arr[i - 1])
                output.append(strt)
                cur_dif = dif
                cnt += 1
                if arr[i - 1] + dif == arr[i] and i == len(arr) - 1:
                    stp = str(arr[i])
                    output.append(stp)
                    cnt = 0
            elif dif == 1 and cnt > 0 and i == len(arr) - 1:
                # print('END! write stop for i=', i)
                stp = str(arr[i])
                output.append(stp)
                cnt = 0
            elif dif != cur_dif and len(output) % 2 != 0:
                # print('!(!=)! write stop for i=', i)
                stp = str(arr[i - 1])
                output.append(stp)
                cnt = 0
            elif dif == 1 and dif == cur_dif and cnt > 0:
                # print('rewrite stop for i=', i)
                stp = arr[i]
                cnt += 1
            elif dif == 0 and cnt > 0:
                # print('!(==)! write stop for i=', i)
                stp = str(arr[i])
                output.append(stp)
                cnt = 0
            else:
                # print('else')
                cnt = 0
            # print(i, ': ', strt, stp, 'd=', dif, 'c=', cnt, output, len(arr))
        return split_transform(output)
    else:
        return output


def split_transform(arr):
    edited = []
    for i in range(1, len(arr), 2):
        txt = '{}->{}'.format(arr[i - 1], arr[i])
        edited.append(txt)
    return edited


def main():
    arr = [1, 2, 3]
    arr_a = [0, 1, 2, 7, 5, 6]
    arr_b = [110, 111, 112, 111, -5, -4, -2, -3, -4, -5, 1, 2, 3]
    arr_c = [1, 2, 4, 5, 7, 8]
    print(arr, summary_ranges(arr))
    print(arr_a, summary_ranges(arr_a))
    print(arr_b, summary_ranges(arr_b))
    print(arr_c, summary_ranges(arr_c))


if __name__ == "__main__":
    main()
