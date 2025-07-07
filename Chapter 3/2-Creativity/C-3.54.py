# A sequence S contains n integers taken from the interval [0,4n], with repetitions
#  allowed. Describe an efficient algorithm for determining an integer
#  value k that occurs the most often in S. What is the running time of your
#  algorithm?

def count_repetition(S):
    dic = {}
    for x in S:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    rep = 0
    k = 0
    for val, num in dic.items():
        if num > rep:
            rep = num
            k = val
    return k
# O(n)
