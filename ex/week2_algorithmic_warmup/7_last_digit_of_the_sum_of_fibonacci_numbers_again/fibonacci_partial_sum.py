# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


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


def fibonacci_partial_sum_fast(m, n):

    sum = (fibonacci_sum_fast(n) - fibonacci_sum_fast(m-1)) % 10

    return sum


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))