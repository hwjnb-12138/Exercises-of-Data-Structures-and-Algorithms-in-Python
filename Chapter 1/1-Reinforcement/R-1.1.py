# Write a short Python function, is_multiple(n, m), that takes two integer
#  values and returns True if n is a multiple of m, that is,n = mi for some
#  integer i,andFalse otherwise.

def is_multiple(n, m):
    return not bool(n % m)

# def is_multiple(n, m):
#     return n % m == 0
