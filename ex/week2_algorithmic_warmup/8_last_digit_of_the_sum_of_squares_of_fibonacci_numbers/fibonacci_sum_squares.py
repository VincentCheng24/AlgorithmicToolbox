# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def get_fibonacci_huge_fast(n):
    fibr = []
    fibr.append(0)
    fibr.append(1)
    fibr.append(1)

    idx = 3
    while fibr[idx-1] != 1 or fibr[idx-2] != 0:
        fibr.append((fibr[idx-2] + fibr[idx-1]) % 10)
        idx += 1

    assert fibr.pop() == 1
    assert fibr.pop() == 0

    rem = n % len(fibr)

    return fibr[rem]


def fibonacci_sum_squares_fast(n):
    return get_fibonacci_huge_fast(n) * get_fibonacci_huge_fast(n+1) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
