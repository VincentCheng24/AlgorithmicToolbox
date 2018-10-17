# Uses python3
def edit_distance(s, t):
    # write your code here
    n = len(s)
    m = len(t)

    # n+1 x m+1 matrix
    d = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        d[i][0] = i

    for j in range(m+1):
        d[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(min(d[i-1][j], d[i][j-1]) + 1, d[i-1][j-1] + cost)

    return d[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
