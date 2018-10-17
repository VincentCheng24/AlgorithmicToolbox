# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    fib = [None] * (n+1)
    fib[0] = 0
    fib[1] = 1
    for idx in range(2, n + 1):
        fib[idx] = (fib[idx - 2] + fib[idx - 1]) % 10

    return fib[n]


def get_fibonacci_last_digit_efficient(n):

    fib = [0, 1]
    if n <= 1:
        return fib[n]

    for idx in range(2, n + 1):
        fib[0], fib[1] = fib[1], (fib[0] + fib[1]) % 10

    return fib[1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))
    # print(get_fibonacci_last_digit_efficient(n))
