# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sqr_sum = 0
sum_sqr = 0

for i in range(1, 101):
    sqr_sum += pow(i, 2)
    sum_sqr += i

sum_sqr = pow(sum_sqr, 2)

print(sum_sqr - sqr_sum)
