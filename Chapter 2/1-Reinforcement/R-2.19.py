# When using the ArithmeticProgression class of Section 2.4.2 with an increment
#  of 128 and a start of 0, how many calls to next can we make
#  before we reach an integer of 2^63 or larger?

class Progression:

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self))for j in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


(2 ** 63 // 128) + 1 = 72057594037927937
