from math import sqrt

def problem3():
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    '''
    n = 600851475143
    prime_factors = []

    for d in range(3, int(sqrt(n)), 2):
        if n % d == 0:
            n /= d
            prime_factors.append(d)

    return prime_factors[len(prime_factors) - 1]


if __name__ == '__main__':
    print(problem3())
