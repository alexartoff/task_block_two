#!/usr/bin/env python
from operator import add, sub, mul, truediv


operators = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':truediv
    }


def rpn_calc(arr):
    stack = []
    for i in arr:
        if isinstance(i, int):
            stack.append(i)
            # print(i, stack)
        else:
            step_result = operators[i](stack.pop(-2), stack.pop(-1))
            stack.append(step_result)
            # print(i, step_result, stack)
    return int(stack[0])


def main():
    # (1 + 2) * 4 / 3 = 15
    arr = [7, 2, 3, '*', '-']
    arr_a = [1, 2, '+', 4, '*', 3, '+']
    arr_b = [1, 2, '+', 4, '*', 3, '/']
    arr_c = [1, 2, '+', 2, '*']
    print(arr, rpn_calc(arr))
    print(arr_a, rpn_calc(arr_a))
    print(arr_b, rpn_calc(arr_b))
    print(arr_c, rpn_calc(arr_c))


if __name__ == "__main__":
    main()
