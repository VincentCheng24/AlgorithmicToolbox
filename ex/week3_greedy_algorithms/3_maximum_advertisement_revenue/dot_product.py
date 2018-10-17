# Uses python3

import sys
import numpy as np
import time


def max_dot_product(a, b):
    # write your code here
    st = time.time()
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]

    print("Normal time is {}".format(time.time() - st))
    return res


def max_dot_product_vector(a, b):
    st = time.time()
    a.sort()
    b.sort()
    res = [y*z for y, z in zip(a, b)]
    res = np.array(res).sum()

    print("Vector time is {}".format(time.time() - st))

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    # print(max_dot_product_vector(a, b))

    # now too few numbers to show the difference