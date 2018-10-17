# Uses python3

import sys
import time
import numpy as np


def islarger(d, m):
    # ld = len(str(d))
    # lm = len(str(m))
    #
    # length = max(ld, lm)
    # dl = abs(ld - lm)
    #
    # if ld > lm:
    #     m = m * 10 ^ dl
    # elif ld < lm:
    #     d = d

    rd = int(str(d)[::-1])
    rm = int(str(m)[::-1])

    firstD = max(rd % 10, rm % 10)

    flag = True

    while flag:

        rrd = rd % 10
        rrm = rm % 10

        if rrd > rrm:
            res = d
            flag = False
        elif rrd > rrm:
            res = m
            flag = False
        else:
            rd = int(rd / 10)
            rm = int(rm / 10)

        if rd == 0 and rm == 0:
            res = m
            flag = False
        if rd == 0 and rm != 0:
            rd = firstD
        if rd != 0 and rm == 0:
            rm = firstD

    return res


def islarger_fast(d, m):

    if m == d:
        return m

    ld = len(d)
    lm = len(m)

    # length = max(ld, lm)
    dl = abs(ld - lm)

    rd = int(d[::-1])
    rm = int(m[::-1])

    if ld > lm:
        strm = m + str(rm % 10) * dl
        rm = int(strm[::-1])
    elif ld < lm:
        strd = d + str(rd % 10) * dl
        rd = int(strd[::-1])

    while True:

        rrd = rd % 10
        rrm = rm % 10

        if rrd > rrm:
            return d
        elif rrd < rrm:
            return m
        else:
            rd = int(rd / 10)
            rm = int(rm / 10)


def largest_number(a):
    # write your code here
    int_a = np.array(a).astype(int)
    max_a = max(int_a)
    id_ma = np.where(int_a == max_a)[0][0]

    l = len(a[id_ma])
    a_equ_len = []

    for ele in a:
        temp = []
        if len(ele) < l:
            temp = ele + ele[0] * (l - len(ele))
        else:
            temp = ele
        a_equ_len.append(temp)

    idx = sorted(range(len(a_equ_len)), reverse=True, key=lambda k: a_equ_len[k])

    res = ""
    for i in idx:
        res += a[i]
    return res


def largest_number_v2(a):
    a.sort(reverse=True)
    res = ""
    while len(a) > 0:
        maxDigit = '0'

        for d in a:
            maxDigit = islarger_fast(d, maxDigit)

        a.remove(maxDigit)
        res += str(maxDigit)

    return res


def largest_number_v3(x):

    maxlen = len(str(max(x)))
    return ''.join(sorted((str(v) for v in x), reverse=True,
                          key=lambda i: i * (maxlen * 2 // len(i))))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    st = time.time()
    print(largest_number_v3(a))
    # print("Time is {}".format(time.time()-st))


# 100 2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5

# x = ['2', '23', '21', '204', '2543']
# y = ['2222', '2322', '2122', '2042', '2543']