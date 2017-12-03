import sys
import glob

def LS(stalls):
    for i in range(0, len(stalls)):
        if stalls[-i]: return i

def RS(stalls):
    for i in range(0, len(stalls)):
        if stalls[i]: return i

def occupyStall(stalls):
    stalls[ int((len(stalls) - 1) * 0.5) ] = True

def findLast(n, k):
    stalls = [False] * (n + 2)
    stalls[0], stalls[-1] = True, True

    """
        To avoid confusion, they follow deterministic rules: For each empty
        stall S, they compute two values Ls and Rs, each of which is the number
        of empty stalls between S and the closest occupied stall to the left or
        right, respectively. Then they consider the set of stalls with the
        farthest closest neighbor, that is, those S for which min(LS, RS) is
        maximal. If there is only one such stall, they choose it; otherwise,
        they choose the one among those where max(LS, RS) is maximal. If there
        are still multiple tied stalls, they choose the leftmost stall among
        those.
    """
    first_index, last_index = int((len(stalls) - 1) * 0.5), 0
    for i in range(0, k):
        if i == 0:
            occupyStall(stalls)
            continue

        left = LS( stalls[:first_index] )
        right = RS( stalls[first_index:] )



    return ""

inputFiles = []
if len(sys.argv) == 2 and str(sys.argv[1]) == "-l": inputFiles = glob.glob('*-large*.in')
elif len(sys.argv) == 2 and str(sys.argv[1]) == "-s": inputFiles = glob.glob('*-small*.in')
else: inputFiles = glob.glob('sample.in')

for fn in inputFiles:
    with open(fn) as f:
        T = int(f.readline())
        lines = [line.strip() for line in f.readlines()]
        N = [int(line.split(" ")[0]) for line in lines]
        K = [int(line.split(" ")[1]) for line in lines]

        for x in range(0, T):
            print( "Case #" + str(x+1) + ": " + findLast(N[x], K[x]) )
