# Describe an efficient recursive function for solving the element uniqueness
#  problem, which runs in time that is at most O(n^2) in the worst case
#  without using sorting.

def recur_unique(s, start=0):
    if start >= len(s):
        return True

    for i in range(start+1, len(s)):
        if s[start] == s[i]:
            return False
    return recur_unique(s, start+1)
