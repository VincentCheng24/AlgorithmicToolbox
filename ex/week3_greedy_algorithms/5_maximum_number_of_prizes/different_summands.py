# Uses python3
import sys


def optimal_summands(n):
    summands = []
    sum = 0
    i = 1
    # write your code here
    while sum < n:
        sum = sum + i
        if sum > n:
            summands[-1] = summands[-1] + n - (sum - i)
            break
        summands.append(i)
        i = i + 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
