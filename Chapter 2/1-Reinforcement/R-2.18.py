# Give a short fragment of Python code that uses the progression classes
#  from Section 2.4.2 to find the 8th value of a Fibonacci progression that
#  starts with 2 and 2 as its first two values.

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


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


fib = FibonacciProgression(2, 2)
for i in range(7):
    next(fib)

print(next(fib))
