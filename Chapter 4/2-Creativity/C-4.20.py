# Given an unsorted sequence, S, of integers and an integer k, describe a
#  recursive algorithm for rearranging the elements in S so that all elements
#  less than or equal to k come before any elements larger than k. What is
#  the running time of your algorithm on a sequence of n values?

def rearrange(S, k, idx=0):
    if idx == len(S):
        return S

    rearrange(S, k, idx + 1)

    if S[idx] > k:
        old = S.pop(idx)
        S.append(old)

    return S
# O(n^2)
