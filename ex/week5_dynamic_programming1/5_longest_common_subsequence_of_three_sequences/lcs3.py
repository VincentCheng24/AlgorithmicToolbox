#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    m = len(a)
    n = len(b)
    p = len(c)

    d = [[[0 for i in range(m + 1)] for j in range(n + 1)] for k in range(p+1)]

    for i in range(p+1):
        for j in range(n+1):
            for k in range(m+1):

                if i*j*k == 0:
                    d[i][j][k] = 0

                elif c[i-1] == b[j-1] and c[i-1] == a[k-1]:
                    d[i][j][k] = d[i-1][j-1][k-1] + 1

                else:
                    d[i][j][k] = max(d[i-1][j][k],d[i][j-1][k],d[i][j][k-1],d[i-1][j-1][k],d[i-1][j][k-1],d[i][j-1][k-1])


    return d[p][n][m]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
