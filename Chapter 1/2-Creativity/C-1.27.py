# In Section 1.8, we provided three different implementations of a generator
#  that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efficient, but we noted that it did not
#  yield the factors in increasing order. Modify the generator so that it reports
#  factors in increasing order, while maintaining its general performance ad-
# vantages.

def sorted_factors(n):
    upper = []
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            upper.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for num in reversed(upper):
        yield num
