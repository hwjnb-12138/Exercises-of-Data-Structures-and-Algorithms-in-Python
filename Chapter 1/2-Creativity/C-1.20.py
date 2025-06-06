# Python’s random module includes a function shuffle(data) that accepts a
#  list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
#  more basic function randint(a, b) that returns a uniformly random integer
#  from a to b (including both endpoints). Using only the randint function,
#  implement your own version of the shuffle function.

def custom_shuffle(data):
    l = len(data)
    for i in range(l):
        tmp = randint(0, l - 1)
        data[i], data[tmp] = data[tmp], data[i]
    return data
