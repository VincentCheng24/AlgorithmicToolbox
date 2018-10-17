# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):
    fibr = []
    fibr.append(0)
    fibr.append(1)
    fibr.append(1)

    idx = 3
    while fibr[idx-1] != 1 or fibr[idx-2] != 0:
        fibr.append((fibr[idx-2] + fibr[idx-1]) % m)
        idx += 1

    assert fibr.pop() == 1
    assert fibr.pop() == 0

    rem = n % len(fibr)

    return fibr[rem]


def get_fibonacci_huge_efficient(n, m):
    if n <= 2:
        return n

    fib = [None] * 3
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    for idx in range(3, n + 1):
        fib[0], fib[1], fib[2] = fib[1], fib[2], (fib[1] + fib[2]) % m

    return fib[2]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
