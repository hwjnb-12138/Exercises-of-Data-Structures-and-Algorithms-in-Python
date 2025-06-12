# Assuming it is possible to sort n numbers in O(nlogn) time, show that it
#  is possible to solve the three-way set disjointness problem in O(nlogn)
#  time.

def three_set_disjointness(A, B, C):
    A = sorted(A)
    B = sorted(B)
    C = sorted(C)

    i = j = k = 0
    while i < len(A) and j < len(B) and k < len(C):
        a = A[i], b = B[j], c = C[k]

        if a == b or a == c or b == c:
            return False

        if a <= b and a <= c:
            i += 1
        elif b <= a and b <= c:
            j += 1
        else:
            k += 1

        return True
