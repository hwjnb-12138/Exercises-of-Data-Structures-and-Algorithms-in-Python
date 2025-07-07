# Use recursion to write a Python function for determining if a string s has
#  more vowels than consonants.

def compare(s, idx=0, vowels=0, consonants=0):
    if idx == len(s):
        return vowels > consonants

    if s[idx].isalpha():
        if s[idx] in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1

    return compare(s, idx+1, vowels, consonants)
