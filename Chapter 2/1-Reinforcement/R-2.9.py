# Implement the __sub__ method for the Vector class of Section 2.3.3, so
#  that the expression u−v returns a new vector instance representing the
#  difference between two vectors.

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result
