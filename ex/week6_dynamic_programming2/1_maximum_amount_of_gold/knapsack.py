# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def maximal_weight(W, w):
    res = [0] * (W+1)
    for i in range((len(w))):
        for j in range(W, w[i]-1, -1):
            res[j] = max(res[j], res[j-w[i]]+w[i])

    return res[W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(maximal_weight(W, w))
