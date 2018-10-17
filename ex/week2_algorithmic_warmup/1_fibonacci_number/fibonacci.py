# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    if n <= 1:
        return n

    fib = [None] * (n+1)
    fib[0] = 0
    fib[1] = 1
    for idx in range(2, n + 1):
        fib[idx] = fib[idx - 2] + fib[idx - 1]

    return fib[n]


n = int(input())
# print(calc_fib(n))
print(calc_fib_fast(n))
