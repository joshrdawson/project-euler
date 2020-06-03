# Find the sum of all the primes below two million.

def sum_prime(n):
    sieve = [True] * n
    solution = 0
    for i in range(2, n):
        if sieve[i]:
            solution += i
            for r in range(i*i, n, i):
                sieve[r] = False
    return solution


print(sum_prime(2000000))
