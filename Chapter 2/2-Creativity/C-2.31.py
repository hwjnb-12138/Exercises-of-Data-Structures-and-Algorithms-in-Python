# Write a Python class that extends the Progression class so that each value
#  in the progression is the absolute value of the difference between the previous
#  two values. You should include a constructor that accepts a pair of
#  numbers as the first two values, using 2 and 200 as the defaults.

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


class AbsoluteProgression(Progression):

    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = first - second

    def _advance(self):
        temp = abs(self._current - self._prev)
        self._prev = self._current
        self._current = temp
