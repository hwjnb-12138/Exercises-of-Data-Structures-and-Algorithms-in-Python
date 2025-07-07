# Describe a recursive algorithm to compute the integer part of the base-two
#  logarithm of n using only addition and integer division.

def logroot(n, res=0):
    if n < 2:
        return res

    return logroot(n//2, res+1)
