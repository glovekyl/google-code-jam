import sys
import glob


def flip(p):
    return "+" if p == "-" else "-"


def findMinFlip(s):
    stack = list(s)
    stackSize, count = len(s), 0
    for i in range(stackSize - 1, -1, -1):
        if stack[i] == "+": continue
        for j in range(i, -1, -1):
            stack[j] = flip(stack[j])
        count += 1

    return str(count)

if len(sys.argv) != 2:
    print("Please enter an input file.")
    exit()

filename = ""
if str(sys.argv[1]) == "-l": filename = glob.glob('*-large-*.in')[0]
elif str(sys.argv[1]) == "-s": filename = glob.glob('*-small-*.in')[0]
else:
    print("Unknown command.")
    exit()

with open(filename) as f:
    T, pancakeStacks = int(f.readline()), [line.strip() for line in f.readlines()]

    for x in range(0, T):
        print("Case #" + str(x+1) + ": " + findMinFlip(pancakeStacks[x]))
