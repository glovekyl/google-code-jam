import math


class Primes:
    """
        Sieve of Eratosthenes is a simple algorithm for finding all prime
        numbers up to any given limit with O(n log log n).

        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """

    def __init__(self, n=2):
        self.__frontier = [False, False]
        self.__extend(n)
        self.__calcPrimes(n)

    def __int__(self):
        return len(self.__frontier)

    def __str__(self):
        temp_list = []
        for i in range(len(self.__frontier)):
            if self.__frontier[i]:
                temp = ', ' + str(i) if i > 2 else str(i)
                temp_list.append(temp)

        return ''.join(temp_list)

    def __extend(self, n):
        self.__frontier.extend([True] * (n - len(self.__frontier) + 1))

    def __calcPrimes(self, n):
        for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
            if self.__frontier[i]:
                k = 1
                for j in range(i**2, n + 1, k*i):
                    self.__frontier[j] = False
                    k += 1

    def isPrime(self, n):
        if n >= len(self.__frontier):
            self.__extend(n)
            self.__calcPrimes(n)
        return self.__frontier[n]
