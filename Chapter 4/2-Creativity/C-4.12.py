# Give a recursive algorithm to compute the product of two positive integers,
#  mand n, using only addition and subtraction.

def product(m, n, res=0):
    if n < 1:
        return res

    return product(m, n-1, res+m)
