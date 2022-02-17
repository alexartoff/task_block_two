#!/usr/bin/env python
# m1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f']
# ]

# m2 = [
#     [1, 2],     [1, 3, 5],
#     [3, 4],     [2, 4, 6]
#     [5, 6]
# ]

# m1*m2 = [
#     [('a1'+'b3'+'c5'), ('a2'+'b4'+'c6')],
#     [('d1'+'e3'+'f5'), ('d2'+'e4'+'f6')]
# ]
# m2*m1 = [
#     [('1a'+'2d'), ('1b'+'2e'), ('1c'+'2f')],
#     [('3a'+'4d'), ('3b'+'4e'), ('3c'+'4f')],
#     [('5a'+'6d'), ('5b'+'6e'), ('5c'+'6f')]
# ]


def multiply(a, b):
    output = []
    b_rot = rotate(b)
    for i in range(len(a)):
        output.append([])
        for j in range(len(b_rot)):
            output[i].append(sum_elem(a[i], b_rot[j]))
    return output


def sum_elem(lst_a, lst_b):
    res = 0
    for (a, b) in zip(lst_a, lst_b):
        res += a * b
    return res


def rotate(mtrx):
    # print(list(zip(*mtrx)), *mtrx, mtrx)
    output = [list(i) for i in zip(*mtrx)]
    # !!! same, but shorter
    # output = []
    # for i in range(len(mtrx[0])):
    #     output.append([])
    #     for j in range(len(mtrx)):
    #         output[i].append(mtrx[j][i])
    return output


def main():
    m1 = [
        [1, 1, 1],
        [2, 2, 2]
    ]
    m2 = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
   

    print(multiply(m2, m1))
    print(multiply(m1, m2))


if __name__ == "__main__":
    main()
