# Uses python3
import sys
import random


def partition3(a, l, r):
    # write your code here
    x = a[l]
    j = l+1
    k = r

    for i in range(l, r + 1):
        if a[i] < x:

            a[i], a[j] = a[j], a[i]
            j += 1
            # k += 1
            # # a[k], a[i] = a[i], a[k]
        elif a[i] > x:
            a[k], a[i] = a[i], a[k]
            k -= 1

    a[l], a[j] = a[j], a[l]

    return j, k


def partition3_v(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            i += 1
        elif a[i] > x:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        else:
            i += 1

    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition2
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)

    m, n = partition3_v(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
