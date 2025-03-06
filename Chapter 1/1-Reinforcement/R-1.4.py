# Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the positive integers smaller than n.

def square_sum(n):
    sum, i = 0, 1
    while i <= n:
        sum += i * i
        i += 1

    return sum
