#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def queens(N, i, a, b, c):
    if i < N:
        for j in range(N):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(N, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)

for solution in queens(N, 0, [], [], []):
    print([[i, j] for i, j in enumerate(solution)])
