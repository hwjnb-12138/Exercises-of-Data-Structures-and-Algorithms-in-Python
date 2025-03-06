# Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the odd positive integers smaller than n

def odd_square_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            sum += i * i

    return sum

# def sum_of_squares(n):
#     total = 0
#     for j in range(1, n+1, 2):
#         total += j * j
#     return total
