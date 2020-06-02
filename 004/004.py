# Find the largest palindrome made from the product of two 3-digit numbers.

biggest = 0
xy = [0, 0]


def is_palindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False


for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        product = x*y
        if is_palindrome(product) and product > biggest:
            biggest = product
            xy = x, y

print('solution found! x=%d y=%d total=%d' % (xy[0], xy[1], biggest))
