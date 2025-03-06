# Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.

res = sum(k * k for k in range(1, n+1) if k % 2 == 1)

# total = sum(j * j for j in range(1, n+1, 2))
