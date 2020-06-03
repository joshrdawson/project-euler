# What is the 10 001st prime number?

TARGET = 10001
number = 1
p_count = 0


def is_prime(p):
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    for i in range(3, p / 2, 2):
        if p % i == 0:
            return False
    return True


while p_count != TARGET:
    number += 1
    if is_prime(number):
        p_count += 1

print(number)
