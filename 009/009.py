# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

goal = 1000

for a in range(1, 333):
    for b in range(a + 1, 500):
        for c in range(b + 1, 997):
            if pow(c, 2) == pow(a, 2) + pow(b, 2) and (a+b+c == goal):
                print('a=%d, b=%d, c=%d\tproduct=%d' % (a, b, c, a*b*c))
