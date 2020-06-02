# What is the largest prime factor of the number 600851475143?

NUMBER = 13195
primes = [2]


def get_max():
    for num in range(3, int(NUMBER / 2), 2):
        for i in range(3, int(num / 2), 2):
            if num % i == 0:
                break
        else:
            if NUMBER % num == 0 and num > primes[-1]:
                primes.append(num)


get_max()

print('prime factors found %s' % (primes))
print('highest factor %d' % (primes[-1]))
