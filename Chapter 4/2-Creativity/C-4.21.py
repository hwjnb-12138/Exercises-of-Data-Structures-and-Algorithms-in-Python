# Suppose you are given an n-element sequence, S, containing distinct integers
#  that are listed in increasing order. Given a number k, describe a
#  recursive algorithm to find two integers in S that sum to k, if such a pair
#  exists. What is the running time of your algorithm?

def sum_k(S, k, res, start=0, end=None):
    if end is None:
        end = len(S) - 1

    if start >= end:
        return res

    if S[start] + S[end] < k:
        sum_k(S, k, res, start+1, end)
    elif S[start] + S[end] > k:
        sum_k(S, k, res, start, end-1)
    else:
        res.append((S[start], S[end]))
        # sum_k(S, k, res, start+1, end-1)

    return res
# O(n)
