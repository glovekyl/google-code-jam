"""
https://code.google.com/codejam/contest/6254486/dashboard#s=p0
"""

import sys
import glob


def solver(n):
    a = int(n)

    # Solver is only infinite if 'N = 0'
    if a == 0:
        print("INSOMNIA")
        return

    # Create a set of unseen digits 0 - 9
    unseen_digits = set(range(10))
    while True:
        # Split current number into set of digits ie: 1223 = {1, 2, 3}
        digits = set(int(d) for d in str(a))

        # Remove found digits from the master set
        unseen_digits = unseen_digits - digits

        # Only break if unseen digits is empty
        if len(unseen_digits) == 0:
            break

        # Increment N
        a += int(n)

    print(a)


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
