# Write a short Python function that counts the number of vowels in a given
#  character string.

def count_vowels(data):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ele in data:
        if ele in vowels:
            count += 1
    return count
