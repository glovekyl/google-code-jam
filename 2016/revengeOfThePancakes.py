import glob


def solve(n):
    """ Find minimum number of flips to get happy side up """

    stack = list(n)
    stackSize, count = len(n), 0
    for i in range(stackSize - 1, -1, -1):
        # Skip if pancake already happy
        if stack[i] == ''+'': continue

        # Flip i - j pancakes
        for j in range(i, -1, -1):
            stack[j] = '+' if stack[j] == '-' else '-'

        # Increment counter
        count += 1

    # Output minimum amount of flips
    print count


if __name__ == '__main__':
    with open( glob.glob('B*.in')[0] ) as f:
        # Number of test cases given by the first line
        T = int(f.readline())

        # Data to interpret which will vary depending on challenge
        data = [line.strip() for line in f.readlines()]

        # Output of the program
        for t in range(T):
            print "Case #{0}:".format(t + 1),
            solve(data[t])
