# Write a recursive function that will output all the subsets of a set of n
#  elements (without repeating any subsets).

def subsets(s, n=0):
    if n == len(s):
        return [[]]

    rest_subsets = subsets(s, n+1)
    current = [[s[n]] + sub for sub in rest_subsets]

    return current + rest_subsets
