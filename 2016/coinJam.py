"""
Latest version does NOT work, I'm in the middle of rewriting it. See older
versions for a working - more complicated - example.
"""

import glob
import itertools

import util


def bin2base(x, base):
    return int(bin(x)[2:], base)


def solve(n):
    n, j = int( n[0] ), int( n[1] )

    perms = ["".join(seq) for seq in itertools.product("01", repeat=n)]

    primes = util.Primes()

    coins = []
    for x in list(perms):
        if x[0] == "1" and x[-1] == "1":
            for i in range(3, 10):
                n = bin2base(int(x), i)
                print("int: " + x + " i: " + str(i) + " n: " + str(n))
                if primes.isPrime(bin2base(int(x), i)): break
            coins.append(x)
        if len(coins) >= j: return

    print("Could not find any more Jam Coins!")

if __name__ == '__main__':
    with open( glob.glob('C*.in')[0] ) as f:
        # Number of test cases given by the first line
        T = int(f.readline())

        # Data to interpret which will vary depending on challenge
        data = [line.split() for line in f.readlines()]

        # Output of the program
        for t in range(T):
            print "Case #{0}:".format(t + 1),
            solve(data[t])
