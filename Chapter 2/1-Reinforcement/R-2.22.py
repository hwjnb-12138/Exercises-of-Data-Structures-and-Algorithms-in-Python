# The collections.Sequence abstract base class does not provide support for
#  comparing two sequences to each other. Modify our Sequence class from
#  Code Fragment 2.14 to include a definition for the __eq__ method, so
#  that expression seq1 == seq2 will return True precisely when the two
#  sequences are element by element equivalent.

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, j):
        pass

    def __eq__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError('Different types cannot be compared')
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
