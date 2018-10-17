# python3
import numpy as np


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_v2(numbers):
   # n = len(numbers)
   # max_product = 0
    first = 0
    second = 0
    for i in numbers:
        if i >= first:
            second = first
            first = i
            continue
        elif i > second:
            second = i

    return first * second


def stress_test():
    while True:
        n_max = 1000
        n = np.random.randint(n_max, size=1)
        print('The n is {}\n'.format(n))

        v_max = 1e4
        vec = np.random.randint(v_max, size=n)
        print(vec)
        #for v in vec:
        #    print('{} '.format(v))

        print('\n')

        res1 = max_pairwise_product(vec)
        res2 = max_pairwise_product_v2(vec)

        if res1 != res2:
            print('wrong answers: res1: {}; res2: {} \n'.format(res1, res2))
            break
        else:
            print('ok')


if __name__ == '__main__':
    stress_test()

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_v2(input_numbers))
