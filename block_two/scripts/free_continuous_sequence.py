#!/usr/bin/env python


def is_continuous_sequence(seque):
    if len(seque) > 1:
        tmp = seque[1] - seque[0]
        for i in range(1, len(seque)):
            dif = seque[i] - seque[i - 1]
            if tmp != dif:
                return False
        return True
    else:
        return False


def main():
    seque = [9, 8 , 7]
    seque_a = [1]
    seque_b = []
    seque_c = [1,2,4,5]
    print(is_continuous_sequence(seque))
    print(is_continuous_sequence(seque_a))
    print(is_continuous_sequence(seque_b))
    print(is_continuous_sequence(seque_c))


if __name__ == "__main__":
    main()
