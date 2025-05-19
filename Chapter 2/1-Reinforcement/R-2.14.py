# Implement the __mul__ method for the Vector class of Section 2.3.3, so
#  that the expression u * v returns a scalar that represents the dot product of
#  the vectors

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __mul__(self, v):
        if not isinstance(v, Vector):
            raise TypeError('v must be a Vector')
        if len(self) != len(v):
            raise ValueError('dimensions must agree')
        result = 0
        for i in range(len(self)):
            result += self[i] * v[i]
        return result
