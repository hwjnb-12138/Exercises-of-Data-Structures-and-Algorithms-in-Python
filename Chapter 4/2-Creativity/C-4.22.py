# Develop a nonrecursive implementation of the version of power
# from Code Fragment 4.12 that uses repeated squaring.

def power(x, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= x

        x *= x
        n //= 2
    return res
