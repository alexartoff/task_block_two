#!/usr/bin/env python


def find_longest_length(txt):
    output = []
    if txt == '':
        return 0
    stop = False
    while not stop:
        txt, output, stop = make_lst(txt, output, stop)
    else:
        output.sort(key=len)
        # print(len(output[-1]), output[-1], output)
        return len(output[-1])


def make_lst(txt, lst, stop):
    tmp = ''
    for ch in txt:
        if is_uniq(ch, tmp):
            tmp += ch
            stop = True
        else:
            lst.append(tmp)
            txt = txt[(txt.find(ch) + 1):]
            stop = False
            return txt, lst, stop
    lst.append(tmp)
    return txt, lst, stop


def is_uniq(ch, txt):
    if txt.count(ch) > 0:
        return False
    return True


def main():
    txt_a = '1234561qweqwer'
    print(find_longest_length(txt_a))


if __name__ == "__main__":
    main()
