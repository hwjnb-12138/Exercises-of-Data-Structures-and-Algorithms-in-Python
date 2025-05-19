# In Section 2.3.3, we note that our Vector class supports a syntax such as
#  v=u+[5,3,10,−2, 1], in which the sum of a vector and list returns
#  a new vector. However, the syntax v=[5,3,10,−2, 1] + u is illegal.
#  Explain how the Vector class definition can be revised so that this syntax
#  generates a new vector.

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __radd__(self, other):
        return self + other
