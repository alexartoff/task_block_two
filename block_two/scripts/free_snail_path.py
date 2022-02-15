#!/usr/bin/env python

# FIXME - переделать этот кошмарный костыль!
# подсказка: поворот мартицы против часовой стрелки
def snail_path(arr):
    output = []
    if len(arr) > 1 and len(arr[0]) == 1:
        for i in arr:
            output.append(i[0])
        return output
    elif len(arr) == 2 and len(arr[0]) == 2:
        return arr[0][:] + arr[1][::-1]
    elif len(arr) > 1:
        # output.append(arr[0][0])
        counter = 0
        while counter >= 0:
            if len(arr[counter][0 + counter:len(arr[0]) - counter]) <= 1:
                output.extend(arr[counter][0 + counter:len(arr[0]) - counter])
                # print('end')
                break
            else:
                output.extend(arr[counter][0 + counter:len(arr[0]) - counter])
                # print(counter, 
                #     '\ttop\t', 
                #     arr[counter][0 + counter:len(arr[0]) - counter])
                for h in range(1 + counter, len(arr) - counter):
                    output.append(arr[h][-1 - counter])
                    # print(counter, h, '\trigth\t', arr[h][-1 - counter])
                output.extend(arr[len(arr) - 1 - counter][len(arr[h]) - 2 - counter:0 + counter:-1])
                # print(counter, h, 
                #     '\tbott\t', 
                #     arr[len(arr) - 1 - counter][len(arr[h]) - 2 - counter:0 + counter:-1])
                for h in range(len(arr) - 1 - counter, 0 + counter, -1):
                    output.append(arr[h][0 + counter])
                    # print(counter, h, '\tleft\t', arr[h][0 + counter])
                counter += 1
            # print(counter, output)
        return output
    elif len(arr) == 1 and len(arr[0]) > 0:
        # print('=1', arr, len(arr))
        return arr[0]
    else:
        # print('None', arr, len(arr))
        return None


def main():
    arr_one = [
        [1],
        [2],
        [3],
        [4]
    ]
    arr_two = [
        ['aa', 'bb', 'cc', 'dd'],
        ['11', 777, [0], None],
        ['zz', True, False, []],
        # ['*', {}, 99],
    ]
    arr_three = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    arr_four = [
        [1, 2],
        [3, 4]
    ]

    arr_fifth = [
        [None, 0, True],
        [-1, '', False],
        [[], 'foo', object],
    ]

    print('1', snail_path(arr_one))
    print('2', snail_path(arr_two))
    print('3', snail_path(arr_three))
    print('4', snail_path(arr_four))
    print('5', snail_path(arr_fifth))


if __name__ == "__main__":
    main()
