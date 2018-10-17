# Uses python3
import sys


def get_change(m):
    # write your code here
    num = 0
    num = m // 4
    r4 = m % 4
    if r4 == 2:
        return num + 1
    else:
        num += r4 // 3
        num += r4 % 3

    return num


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
