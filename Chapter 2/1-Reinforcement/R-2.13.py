# Exercise R-2.12 asks for an implementation of __mul__, for the Vector
#  class of Section 2.3.3, to provide support for the syntax v * 3. Implement
#  the __rmul__ method, to provide additional support for syntax 3 * v.

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("n must be a numeric type.")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * n
        return result

    def __rmul__(self, n):
        return self * n
