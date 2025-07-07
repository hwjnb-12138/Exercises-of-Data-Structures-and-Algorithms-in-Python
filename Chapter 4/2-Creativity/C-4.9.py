# Write a short recursive Python function that finds the minimum and
# maximum values in a sequence without using any loops.

def min_max(S):
    if len(S) == 1:
        return S[0], S[0]

    mintmp, maxtmp = min_max(S[1:])
    mini = S[0]
    maxi = S[0]
    if mini > mintmp:
        mini = mintmp
    if maxi < maxtmp:
        maxi = maxtmp

    return mini, maxi
