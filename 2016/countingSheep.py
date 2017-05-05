import glob


def solve(n):
    if int(n) is 0: return "INSOMNIA"
    di = list(range(0, 10))

    i = 1
    while len(di) > 0:
        n_str = [int(d) for d in str(i * int(n))]
        for s in n_str:
            if s in di:
                di.remove(int(s))

            if not di:
                print str(int(n) * i)
                return
        i += 1


if __name__ == '__main__':
    with open( glob.glob('A*.in')[0] ) as f:
        # Number of test cases given by the first line
        T = int(f.readline())

        # Data to interpret which will vary depending on challenge
        data = [line.strip() for line in f.readlines()]

        # Output of the program
        for t in range(T):
            print "Case #{0}:".format(t + 1),
            solve(data[t])
