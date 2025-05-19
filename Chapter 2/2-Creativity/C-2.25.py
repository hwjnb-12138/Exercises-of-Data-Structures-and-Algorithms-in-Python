# Exercise R-2.12 uses the __mul__ method to support multiplying a Vector
#  by a number, while Exercise R-2.14 uses the __mul__ method to support
#  computing a dot product of two vectors. Give a single implementation of
#  Vector.__mul__ that uses run-time type checking to support both syntaxes
#  u * v and u * k,where u and v designate vector instances and k represents
#  a number.

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = other * self[i]
            return result
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i]
            return result
