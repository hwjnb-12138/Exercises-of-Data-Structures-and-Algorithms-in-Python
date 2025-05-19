# Implement the __neg__ method for the Vector class of Section 2.3.3, so
#  that the expression −v returns a new vector instance whose coordinates
#  are all the negated values of the respective coordinates of v.

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
