# Describe a recursive algorithm for finding the maximum element in a
# sequence, S, of n elements. What is your running time and space usage?

def find_seq_max(S, n):
    if n == 1:
        return S[0]

    seq_max = find_seq_max(S, n-1)
    current = S[n-1]
    return current if current > seq_max else seq_max

# running time: O(n)
# space usage: O(n)
