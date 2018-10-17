# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_efficient(n):
    if n <= 1:
        return n

    sum = 1
    a = 0
    b = 1
    for idx in range(2, n + 1):

        a, b = b, (a+b)%10
        sum = (sum + b) % 10

        print(idx, sum)

    return sum


def fibonacci_sum_fast(n):
    # fibonacci_sum_efficient(n)
    fibr = []
    fibr.append(0)
    fibr.append(1)
    fibr.append(2)

    sum = 2
    a = 1
    b = 1

    idx = 3
    while fibr[idx-1] != 1 or fibr[idx-2] != 0:
        a, b = b, (a + b) % 10
        sum = (sum + b) % 10

        fibr.append(sum)
        idx += 1

        # print(idx, sum)

    assert fibr.pop() == 1
    assert fibr.pop() == 0

    rem = n % len(fibr)

    return fibr[rem]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
