#!/usr/bin/env python


def chunked(num, frame):
    output = []
    if len(frame) <= num and len(frame) != 0:
        output.append(frame[:])
        return output
    elif len(frame) > num:
        chunks = len(frame) // num
        for i in range(chunks):
            # print(i, (i * num), (i * num + num), chunks)
            output.append(frame[(i * num):(i * num + num)])
        if len(frame) % num != 0:
            output.append(frame[(chunks * num):])
        return output
    else:
        return output


def main():
    frame = ['a', 'b', 'c', 'd']
    frame_a = ('a', 'b', 'c', 'd', 'e')
    frame_b = 'abcde'
    frame_c = ''
    frame_d = 'a'
    print(chunked(2, frame))
    print(chunked(2, frame_a))
    print(chunked(2, frame_b))
    print(chunked(2, frame_c))
    print(chunked(2, frame_d))


if __name__ == "__main__":
    main()
