#!/usr/bin/env python


def find_longest_length(txt):
    ntxt = txt[:1]
    for ch in txt:
        print('for ch={} in txt >>> ntxt={}'.format(ch, ntxt))
        if check_str(ch, ntxt):
            ntxt += ch
            # print('+++', ntxt, ch)
        else:
            ntxt += ''
            # print('---', ntxt, ch)
    print(ntxt, len(ntxt))


def check_str(ch, txt):
    print('>>> ch="{}" - ntxt="{}"'.format(ch, txt))
    if txt.count(ch) >= 1:
        return False
    else:
        return True


def main():
    txt_a = '1234561qweqwer'
    txt_b = 'a'
    print(find_longest_length(txt_a))


if __name__ == "__main__":
    main()
