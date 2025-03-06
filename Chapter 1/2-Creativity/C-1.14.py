# Write a short Python function that takes a sequence of integer values and
#  determines if there is a distinct pair of numbers in the sequence whose
#  product is odd.

def has_odd_product(data):
    l = len(data)
    for i in range(l):
        for j in range(i + 1, l):
            if (data[i] * data[j]) % 2 == 1:
                return True
    return False

# def has_odd_pair(data):
#     count = 0
#     for j in range(len(data)):
#         if data[j] % 2 == 1:
#             count += 1
#             if count == 2:
#                 return True
#     return False
