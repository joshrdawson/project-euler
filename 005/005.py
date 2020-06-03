# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

solution = 20


def divisable(num):
    for i in range(1, 20):
        if num % i != 0:
            return False
    return True


while True:
    if solution % 20 == 0 and divisable(solution):
        break
    else:
        solution += 20


print(solution)
