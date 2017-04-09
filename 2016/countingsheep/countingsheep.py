"""
https://code.google.com/codejam/contest/6254486/dashboard#s=p0
"""

import sys
import glob

if len(sys.argv) != 2:
    print("Please enter an input file.")
    exit()

filename = ""
if str(sys.argv[1]) == "-l": filename = glob.glob('*-large-*.in')[0]
elif str(sys.argv[1]) == "-s": filename = glob.glob('*-small-*.in')[0]
else:
    print("Unknown command.")
    exit()


def findNumber(n):
    if int(n) is 0: return "INSOMNIA"
    di = list(range(0, 10))

    i = 1
    while True:
        n_str = [int(d) for d in str(i * int(n))]
        for s in n_str:
            if s in di: di.remove(int(s))
            if not di: return str(int(n) * i)
        i += 1

with open(filename) as f:
    T, numbers = int(f.readline()), [line.strip() for line in f.readlines()]

for x in range(0, T):
    print("Case #" + str(x+1) + ": " + findNumber(numbers[x]))
