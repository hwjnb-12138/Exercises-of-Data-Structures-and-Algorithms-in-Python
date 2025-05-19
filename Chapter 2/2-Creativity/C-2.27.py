# In Section 2.3.5, we note that our version of the Range class has implicit
#  support for iteration, due to its explicit support of both __len__
#  and __getitem__. The class also receives implicit support of the Boolean
#  test, “k in r” for Range r. This test is evaluated based on a forward iteration
#  through the range, as evidenced by the relative quickness of the test
#  2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
#  more efficient implementation of the __contains__ method to determine
#  whether a particular value lies within a given range. The running time of
#  your method should be independent of the length of the range.

class Range:

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step
        self._stop = stop

    def __contains__(self, k):
        if self._step > 0:
            valid_interval = self._start <= k < self._stop
        else:
            valid_interval = self._stop < k <= self._start
        if not valid_interval:
            return False

        delta = k - self._start
        return not delta % self._step
