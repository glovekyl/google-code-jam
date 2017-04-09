import sys
import glob

A = [False, False]


def bin2base(x, base):
    return int(bin(x)[2:], base)


def isPrime(x):
    import math

    if x >= len(A):
        A.extend([True] * (x - len(A) + 1))

    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if A[i]:
            k = 1
            for j in range(i**2, x+1, k*i):
                A[j] = False
                k += 1

    return A[x]


def getJamCoins(n, j):
    import itertools

    perms = ["".join(seq) for seq in itertools.product("01", repeat=n)]
    coins = []
    for x in list(perms):
        if x[0] == "1" and x[-1] == "1":
            for i in range(3, 10):
                n = bin2base(int(x), i)
                print("int: " + x + " i: " + str(i) + " n: " + str(n))
                if isPrime(bin2base(int(x), i)): break
            coins.append(x)
        if len(coins) >= j: return

    print("Could not find any more Jam Coins!")

if len(sys.argv) != 2:
    print("Please enter an input file.")
    exit()

filename = ""
if str(sys.argv[1]) == "-l": filename = glob.glob('*-large-*.in')[0]
elif str(sys.argv[1]) == "-s": filename = glob.glob('*-small-*.in')[0]
else:
    getJamCoins(int(sys.argv[1]), 50)
    exit()

with open(filename) as f:
    T = int(f.readline())
    N, J = int(f.readline())

print("Case #1:")


