# Write a short Python function that takes a string s, representing a sentence,
#  and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let's try, Mike.", this function would return
#  "Lets try Mike".

import string

def remove_punctuation(s):
    res = []
    for char in s:
        if char not in string.punctuation:
            res.append(char)
    return ''.join(res)
