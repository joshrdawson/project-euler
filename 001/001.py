# Find the sum of all the multiples of 3 or 5 below 1000.

sum_nat = 0

for n in range(1000):
    sum_nat += n if n % 3 == 0 or n % 5 == 0 else 0

print(sum_nat)
