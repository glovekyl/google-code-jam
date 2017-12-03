"""
https://code.google.com/codejam/contest/6254486/dashboard#s=p1
"""

import sys
import glob


def solver(n):
    flips = 0
    # Increment flip for each parallel pancake not equivalent to its partner
    for i in range(1, len(n)):
        if n[i] != n[i-1]:
            flips += 1

    # No need to for additional flip if bottom pancake is happy
    if n[-1] == '+':
        print(flips)
    else:
        print(flips + 1)


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
