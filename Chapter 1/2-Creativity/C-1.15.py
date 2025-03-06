# Write a Python function that takes a sequence of numbers and determines
#  if all the numbers are different from each other (that is, they are distinct).

def check_repeat(data):
    l = len(data)
    for i in range(l):
        for j in range(i + 1, l):
            if data[i] == data[j]:
                return False
    return True
