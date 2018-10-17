# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def dp_sequence(n):
    sequence = []
    a = [0] * (n+1)

    # construct the sequence
    for i in range(1, len(a)):
        a[i] = a[i-1] + 1

        if i % 2 == 0:
            a[i] = min(a[i//2] + 1, a[i])

        if i % 3 == 0:
            a[i] = min(a[i//3]+1, a[i])

    while n > 1:
        sequence.append(n)
        if n%3 == 0 and a[n] == a[int(n/3)] + 1:
            n = int(n/3)
        elif n%2 == 0 and a[n] == a[int(n/2)] + 1:
            n = int(n/2)
        elif a[n] == a[n-1]+1:
            n = n - 1

    sequence.append(1)
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(dp_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
