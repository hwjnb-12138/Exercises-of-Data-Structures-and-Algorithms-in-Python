# Write a short Python program that takes two arrays a and b of length n
#  storing int values, and returns the dot product of a and b. That is, it returns
#  an array c of length n such that c[i]=a[i]·b[i],for i = 0,...,n−1.

def dot_product(a, b, n):
    c = list()
    for i in range(n):
        c.append(a(i) * b(i))
    return c

# return [a[k] * b[k] for k in range(n)]
