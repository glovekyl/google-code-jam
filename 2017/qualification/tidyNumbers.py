"""
https://code.google.com/codejam/contest/3264486/dashboard#s=p1
"""

import sys
import glob


def solver(n):
    m = list(map(int, n))
    if len(m) == 1:
        print(n)
        return

    # Start from the end digit and work back
    for i in range(len(m)-1, 0, -1):
        if m[i] < m[i-1]:
            m[i:] = [9] * len(m[i:])
            m[i-1] -= 1

    # Remove start digit if == '0' print list as complete string
    if m[0] == 0:
        del m[0]
    print(''.join(map(str, m)))


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
