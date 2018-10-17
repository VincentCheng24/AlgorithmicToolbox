# Uses python3

import sys

def lcs2_continuous(a, b):
    # write your code here
    m = len(a)
    n = len(b)

    d = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            x = i
            y = j
            while a[y] == b[x]:
                d[i][j] += 1
                x += 1
                y += 1
                if y >= m:
                    break
                if x >= n:
                    break

    return max(max(d))


def lcs2(a, b):
    # write your code here
    m = len(a)
    n = len(b)

    d = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if j == 0 or i == 0:
                d[i][j] = 0

            elif a[j-1] == b[i-1]:
                d[i][j] = d[i-1][j-1] + 1

            else:
                d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1])

    return d[n][m]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
