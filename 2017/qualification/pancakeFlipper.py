"""
https://code.google.com/codejam/contest/3264486/dashboard#s=p0
"""

import sys
import glob


def solver(n):
    temp = (i for i in n.split(' '))
    cakes = list(next(temp))
    k = int(next(temp))

    flips = 0
    for i in range(0, len(cakes) - k + 1):
        if cakes[i] == '-':
            for j in range(0, k):
                cakes[i + j] = '+' if cakes[i+j] == '-' else '-'
            flips += 1

    if '-' in cakes:
        print("IMPOSSIBLE")
    else:
        print(flips)


if __name__ == "__main__":
    try:
        with open(glob.glob('*' + sys.argv[1] + '*')[0]) as f:
            T = int(f.readline())
            lines = f.readlines()
            for z in range(T):
                print("CASE #{0}: ".format(z + 1), end='')
                solver(lines[z].rstrip("\n\r"))

    except FileNotFoundError:
        print("File does not exist!")
    except IndexError:
        print("Enter input name!")
