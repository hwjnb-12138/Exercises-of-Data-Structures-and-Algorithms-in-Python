# In similar spirit to the previous problem, augment the Sequence class with
#  method __lt__,to support lexicographic comparison seq1 < seq2.

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, j):
        pass

    def __lt__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError('Different types cannot be compared')
        for i in range(min(len(self), len(other))):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False
        return len(self) < len(other)
