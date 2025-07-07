# Write a short recursive Python function that rearranges a sequence of integer
# values so that all the even values appear before all the odd values

def rearrange(s):
    if len(s) <= 1:
        return s

    if s[0] % 2 == 0:
        return [s[0]] + rearrange(s[1:])
    else:
        return rearrange(s[1:]) + [s[0]]
