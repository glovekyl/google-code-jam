"""
https://code.google.com/codejam/contest/3264486/dashboard#s=p0
This is a reimplementation of the previous brute force, simple cleanup and
implemented with a simpler file reader just passes the line straight through
and is purposefully made to read a single file.
"""

import sys
import glob


def solver(n):
    temp = (i for i in n.split(' '))
    cakes = list(next(temp))
    k = int(next(temp))

    flips = 0
    # Flip the pancakes from left to right via brute force
    for i in range(0, len(cakes) - k + 1):
        if cakes[i] == '-':
            for j in range(0, k):
                # Inverse pancakes over range
                cakes[i + j] = '+' if cakes[i+j] == '-' else '-'
            flips += 1

    # Impossible if a plain face pancake exists
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
