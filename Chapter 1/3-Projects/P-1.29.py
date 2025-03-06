# Write a Python program that outputs all possible strings formed by using
#  the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once.

# reference answer
def permute(bag, permutation):
    # When the bag is empty, a full permutation exists
    if len(bag) == 0:
        print(''.join(permutation))
    else:
        # For each element left in the bag
        for k in range(len(bag)):
            # Take the element out of the bag and put it at the end of the permutation
            permutation.append(bag.pop(k))
            # Permute the rest of the bag (recursively)
            permute(bag, permutation);
            # Take the element off the permutation and put it back in the bag
            bag.insert(k, permutation.pop())

permute(list('catdog'), [])
