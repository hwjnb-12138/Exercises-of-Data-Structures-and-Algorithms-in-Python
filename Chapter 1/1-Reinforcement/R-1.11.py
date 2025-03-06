# Demonstrate how to use Python’s list comprehension syntax to produce
#  the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

l = list()
for i in range(0, 9):
    l.append(2 ** i)

# [2 ** k for k in range(9)]
