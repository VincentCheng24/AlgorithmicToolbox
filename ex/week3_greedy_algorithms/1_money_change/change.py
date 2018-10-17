# Uses python3
import sys


def get_change(m):
    # write your code here
    num = 0
    if m >= 10:
        num = num + int(m/10)
        m = m % 10
    if m >= 5:
        num = num + int(m/5)
        m = m % 5
    num = num + m

    return num


def get_change_v2(m):
    # write your code here
    num = 0

    num = num + int(m/10)
    m = m % 10

    num = num + int(m/5)
    m = m % 5

    num = num + m

    return num


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
