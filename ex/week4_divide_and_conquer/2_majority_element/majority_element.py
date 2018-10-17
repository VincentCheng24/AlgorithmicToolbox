# Uses python3
import sys
import numpy as np


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    return -1

# region  problematic

def partition(a, left, right):
    k = np.random.randint(left, right)
    a[k], a[left] = a[left], a[k]

    x = a[left]
    j = left

    for i in range(left+1, right+1):
        if a[i] < x:
            j += 1
            a[j], a[i] = a[i], a[j]

    a[left], a[j] = a[j], a[left]

    return j


def quick_sort(a, left, right):
    if left >= right:
        return a



    m = partition(a, left, right)

    quick_sort(a, left, m - 1)
    quick_sort(a, m + 1, right)


# endregion


def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part



def get_m_via_dict(a, left, right):
    d = {}
    for ele in a:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1

    for key in d:
        if d[key] > right/2:
            return 1

    return -1


def get_m_via_sort(a):
    quicksort(a)

    half = int(len(a)/2)

    for i in range(half):
        if a[i] == a[half]:
            return 1

    return -1


if __name__ == '__main__':
    a = [4, 2, 2, 9, 2, 3, 2]

    # print(get_m_via_sort(a))

    quick_sort(a, 0, len(a)-1)
    print(a)
    # print(a)
    # b = quicksort(a)
    # print(b)



    # print(get_m_via_dict(a, 0, len(a)))


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     if get_m_via_dict(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)
