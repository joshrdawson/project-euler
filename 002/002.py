# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib = 0
prevprev = 0
prev = 1
fib_sum = 0

while fib < 4000000:
    temp = prev
    fib = prev + prevprev
    prevprev = temp
    prev = fib
    fib_sum += fib if fib % 2 == 0 else 0

print(fib_sum)
