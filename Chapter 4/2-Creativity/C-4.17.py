# Write a short recursive Python function that determines if a string s is a
#  palindrome, that is, it is equal to its reverse. For example, ‘racecar’ and
#  ‘gohangasalamiimalasagnahog’ are palindromes.

def is_palindrome(s, start=0, end=None):
    if end is None:
        end = len(s) - 1

    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome(s, start+1, end-1)
