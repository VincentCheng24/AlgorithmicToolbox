# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    current_gcd = 1

    big = max(a, b)
    small = min(a, b)

    if small == 0:
        return big

    while small != 0:
        big, small = small, big % small

    return big


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd_fast(a, b))
